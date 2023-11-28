from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.product import product_router
from routes.user import user_router
from routes.site import site_router
from routes.delivery_person import delivery_person_router  # Importa el nuevo router de delivery persons
from routes.order import order_router
from routes import files_router
from routes.auth import auth
app = FastAPI()

# Configuración para permitir todos los orígenes (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)
app.include_router(user_router)
app.include_router(site_router)
app.include_router(delivery_person_router)
app.include_router(order_router)
app.include_router(files_router.router)
app.include_router(auth) # Incluye el nuevo router de delivery persons
