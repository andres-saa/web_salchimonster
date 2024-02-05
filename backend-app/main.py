from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.product import product_router
from routes.user import user_router
from routes.site import site_router
from routes.delivery_person import delivery_person_router  # Importa el nuevo router de delivery persons
from routes.order import order_router
from routes import files_router
from routes.auth import auth
from routes.category import category_router
from routes.adicional import adicional_router,salsa_router,topping_router,acompanante_router,cambio_router
from routes.grupo_adicionales import grupo_adicionales_router,grupo_toppings_router,grupo_salsas_router,grupo_cambios_router,grupo_acompanantes_router
from routes.employer import employer_router
from routes.site_document import site_document_router
from routes.login import login
from routes.permission import permission_router
from routes.form import form_router
from routes.training import training_router, attendee_router, assigned_attendee_router
from routes.training_document import training_document_router
from routes.training_file import training_file_router
from routes.mail import mail_router
app = FastAPI()
from routes.area import area_router
from routes.role import role_router, rolegroup_router
from routes.city import city_router
from routes.neighborhood import neighborhood_router


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
app.include_router(category_router)
app.include_router(grupo_adicionales_router)
app.include_router(adicional_router)
app.include_router(auth)
app.include_router(topping_router)
app.include_router(acompanante_router)
app.include_router(salsa_router)
app.include_router(grupo_toppings_router)
app.include_router(cambio_router) 
app.include_router(grupo_salsas_router) 
app.include_router(grupo_cambios_router) 
app.include_router(grupo_acompanantes_router) 
app.include_router(employer_router) 
app.include_router(site_document_router)
app.include_router(area_router)
app.include_router(login)
app.include_router(permission_router)
app.include_router(form_router)
app.include_router(training_router)
app.include_router(attendee_router)
app.include_router(assigned_attendee_router)
app.include_router(training_document_router)
app.include_router(training_file_router)
app.include_router(mail_router)
app.include_router(role_router)
app.include_router(rolegroup_router)
app.include_router(city_router)
app.include_router(neighborhood_router)

