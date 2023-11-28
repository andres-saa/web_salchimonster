import { URI } from "./conection";

 function uploadPDF(pdfFile,type_document,site_name) {
    // URL del servidor donde deseas enviar el PDF
    const serverURL = `${URI}/upload-site-documet/`;
  
    // Crear un objeto FormData para enviar el archivo
    const formData = new FormData();
    formData.append('file', pdfFile);
    formData.append('type_document', type_document);
    formData.append('site_name', site_name);
  
    // Realizar una solicitud POST al servidor
    fetch(serverURL, {
      method: 'POST',
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          // La carga fue exitosa, realiza alguna acción si es necesario
          console.log('Archivo PDF cargado con éxito');
        } else {
          console.error('Error al cargar el archivo PDF:', response.status, response.statusText);
        }
      })
      .catch((error) => {
        console.error('Error en la solicitud:', error);
      });
  }
  

   function uploadUserPhotoProfile(photoProfile,id) {
    // URL del servidor donde deseas enviar el PDF
    const serverURL = `${URI}/upload-user-photo-profile/${id}`;
  
    // Crear un objeto FormData para enviar el archivo
    const formData = new FormData();
    formData.append('file', photoProfile);
    
  
    // Realizar una solicitud POST al servidor
    fetch(serverURL, {
      method: 'POST',
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          // La carga fue exitosa, realiza alguna acción si es necesario
          console.log('Archivo photo cargado con éxito');
        } else {
          console.error('Error al cargar foto de perfil:', response.status, response.statusText);
        }
      })
      .catch((error) => {
        console.error('Error en la solicitud:', error);
      });
  }


  // Ejemplo de uso:
//   const inputElement = document.getElementById('pdfInput'); // Obtén el elemento de entrada de archivo
//   inputElement.addEventListener('change', (event) => {
//     const pdfFile = event.target.files[0];
//     if (pdfFile) {
//       uploadPDF(pdfFile);
//     }
//   });

  
  export {uploadPDF,uploadUserPhotoProfile}
  
  