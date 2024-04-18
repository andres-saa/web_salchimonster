from fastapi import FastAPI, Depends, HTTPException, WebSocket, APIRouter,WebSocketDisconnect
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from typing import List, Dict

auth = APIRouter()

# Secret key to sign the JWT token (change this in production)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# Model for the site with username and password
class Site:
    def __init__(self, site_id: int, site_name: str,  username: str = "", password: str = ""):
        self.site_id = site_id
        self.site_name = site_name
        self.username = username
        self.password = password

# List of sites with usernames and passwords
sites = [
    Site(
        site_id=1,
        site_name="CALI_BRETAÑA",
        username="salchi_bretna",
        password="salchi_bretna_3979"
    ),
    Site(
        site_id=2,
        site_name="CALI_LAFLORA",
        username="salchi_laflora",
        password="salchi_laflora_7255"
    ),
    Site(
        site_id=3,
        site_name="CALI_CANEY",
        username="salchi_caney",
        password="salchi_caney_7941"
    ),
    Site(
        site_id=4,
        site_name="CALI_JAMUNDI",
        username="salchi_jamundi",
        password="salchi_jamundi_4948"
    ),
    Site(
        site_id=5,
        site_name="PALMIRA",
        username="salchi_palmira",
        password="salchi_palmira_902"
    ),
    Site(
        site_id=6,
        site_name="TULUA",
        username="salchi_tulua",
        password="salchi_tulua_3714"
    ),
    Site(
        site_id=7,
        site_name="BOGOTA_MODELIA",
        username="salchi_modelia",
        password="salchi_modelia_6439"
    ),
    Site(
        site_id=8,
        site_name="BOGOTA_SUBA",
        username="salchi_suba",
        password="salchi_suba_2936"
    ),
    Site(
        site_id=9,
        site_name="BOGOTA_MONTES",
        username="salchi_montes",
        password="salchi_montes_8785"
    ),
    Site(
        site_id=10,
        site_name="BOGOTA_KENNEDY",
        username="salchi_kennedy",
        password="salchi_kennedy_1974"
    ),
    Site(
        site_id=11,
        site_name="MEDELLIN_LAURELES",
        username="salchi_laureles",
        password="salchi_laureles_0433"
    ),
        Site(
        site_id=12,
        site_name="pueba",
        username="admin-fotos",
        password="admin-fotos-sm"
    ),
]


# Configuración del esquema de seguridad
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Función para verificar las credenciales del usuario
def verify_user(username: str, password: str):
    for site in sites:
        if site.username == username and site.password == password:
            return site

# Ruta para obtener un token de acceso

@auth.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    site = verify_user(form_data.username, form_data.password)
    if site:
        token_data = {"sub": form_data.username}
        token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token,"site_name":site.site_name, "token_type": "bearer", "username": form_data.username, "site_id": site.site_id}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@auth.get("/private-data")
async def get_private_data(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        site = next((s for s in sites if s.username == payload["sub"]), None)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})
    if site:
        return {"message": "Private Data", "username": payload["sub"], "site_id": site.site_id}
    else:
        raise HTTPException(status_code=401, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, site_id: int):
        await websocket.accept()
        if site_id not in self.active_connections:
            self.active_connections[site_id] = []
        self.active_connections[site_id].append(websocket)

    def disconnect(self, websocket: WebSocket, site_id: int):
        if site_id in self.active_connections:
            self.active_connections[site_id].remove(websocket)
            if not self.active_connections[site_id]:
                del self.active_connections[site_id]

manager = ConnectionManager()


    