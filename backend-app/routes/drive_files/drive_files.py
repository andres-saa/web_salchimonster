from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import tempfile
import os
# Initialize router
drive_file_router = APIRouter()

# Initialize GoogleAuth and configure OAuth settings
gauth = GoogleAuth()
gauth.settings['oauth_scope'] = ['https://www.googleapis.com/auth/drive']
gauth.settings['get_refresh_token'] = True  # Ensure we get a refresh token
credentials_file = "credentials_module.json"

# Load credentials on startup
gauth.LoadCredentialsFile(credentials_file)

def authorize_google_drive():
    try:
        if not gauth.credentials:
            raise HTTPException(status_code=500, detail="Error: Could not load credentials")
        if gauth.access_token_expired:
            gauth.Refresh()
            gauth.SaveCredentialsFile(credentials_file)
        else:
            gauth.Authorize()
        return GoogleDrive(gauth)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error authorizing Google Drive: {str(e)}")

@drive_file_router.get("/files-list/{folder_id}")
async def list_files(folder_id: str):
    try:
        authorize_google_drive()

        # Initialize GoogleDrive instance with authenticated credentials
        drive = GoogleDrive(gauth)

        # List all files in the specified Google Drive folder
        file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

        # Extract file names and IDs
        files = [{"file_name": file['title'], 
                  "thumbnailLink": file.get("thumbnailLink", ""), 
                  "file_id": file['id'], 
                  "embedLink": file.get("embedLink", ""), 
                  "alternateLink": file.get("alternateLink", "")} 
                 for file in file_list]

        return {"files": files}

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing files: {str(e)}")



@drive_file_router.delete("/delete-file/{file_id}")
async def delete_file(file_id: str):
    try:
        drive = authorize_google_drive()

        # Initialize GoogleDrive instance with authenticated credentials
        gd_file = drive.CreateFile({'id': file_id})
        gd_file.Delete()

        return {"message": f"File with ID: {file_id} has been deleted successfully"}

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting file: {str(e)}")



@drive_file_router.post("/upload-file")
async def upload_file(
    file: UploadFile = File(...), 
    folder_id: str = Form(...), 
    custom_file_name: str = Form(...)
):
    try:
        authorize_google_drive()

        # Initialize GoogleDrive instance with authenticated credentials
        drive = GoogleDrive(gauth)

        # Function to upload file to Google Drive
        def upload_to_drive(file, folder_id, file_name):
            try:
                file_metadata = {
                    'title': file_name,
                    'parents': [{'id': folder_id}]
                }
                temp_file_path = None

                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file_path = temp_file.name
                    for chunk in iter(lambda: file.file.read(4096), b""):
                        temp_file.write(chunk)

                gd_file = drive.CreateFile(file_metadata)
                gd_file.SetContentFile(temp_file_path)
                gd_file.Upload()

                os.remove(temp_file_path)  # Eliminar archivo temporal después de subirlo

                return gd_file['id']
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")

        # Upload the file
        file_id = upload_to_drive(file, folder_id, custom_file_name)

        return {"message": f"File uploaded successfully with ID: {file_id}"}

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")


@drive_file_router.get("/files-auth")
async def check_auth():
    try:
        # Attempt to load saved credentials
        gauth.LoadCredentialsFile(credentials_file)

        if not gauth.credentials:
            # If no saved credentials, perform local web server authentication
            gauth.LocalWebserverAuth()
            # Save credentials for future runs
            gauth.SaveCredentialsFile(credentials_file)
        elif gauth.access_token_expired:
            # If the access token has expired, refresh the token
            gauth.Refresh()
            # Save updated credentials
            gauth.SaveCredentialsFile(credentials_file)
        else:
            # Authorize current credentials if not expired
            gauth.Authorize()
        
        return {"message": "Authentication successful"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
