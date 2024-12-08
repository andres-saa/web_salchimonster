from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.product import product_router
from routes.user import user_router
from routes.site import site_router
from routes.delivery_person import delivery_person_router 
from routes.drive_files.drive_files import drive_file_router # Importa el nuevo router de delivery persons
# from routes.order import order_router
from routes.orders.order import order_router
from routes.inventory.daily_inventory import daily_inventory_router
from routes.inventory.monthly_inventory import monthly_inventory_router
from routes.inventory.cdi_inventory import cdi_inventory_router
from routes import files_router
from routes.auth import auth
from routes.category import category_router
from routes.adicional import adicional_router,salsa_router,topping_router,acompanante_router,cambio_router
from routes.grupo_adicionales import grupo_adicionales_router,grupo_toppings_router,grupo_salsas_router,grupo_cambios_router,grupo_acompanantes_router
from routes.employer.employer import employer_router
from routes.site_document import site_document_router
from routes.login import login
from routes.permission import permission_employer_router
from routes.form import form_router
from routes.training import training_router, attendee_router, assigned_attendee_router
from routes.training_document import training_document_router
from routes.training_file import training_file_router
from routes.mail import mail_router
from routes.audit import audit_router
from routes.shift_work_scheduler import shift_work_day_router, shift_work_record_router, shift_work_shift_router
from routes.maintenance import maintenance_router, equipment_router
from routes.recipe.ingredient import ingredient_router
from routes.recipe.data_sheet import recipe_data_sheet_router
from routes.aditional_new import adicional_new_router
from routes.inventory.order_purchase import order_purchase_router
from routes.role import role_router, rolegroup_router
from routes.city import city_router
from routes.neighborhood import neighborhood_router
from routes.supply.supply import supply_router
from routes.supply.supply_delivery import supply_delivery_router
from routes.supply.supply_delivery_item import supply_delivery_item_router
from routes.archived_file import archivedFiles_router,areas_router,types_router
from routes.site_schedule import site_schedule_router
from routes.work_scheduler import work_record_router
from routes.work_scheduler import work_shift_router
from routes.work_scheduler import work_day_router
from routes.recipe.recipe import recipe_router
from routes.contests.contest import contest_router
from routes.pqrs.pqrs import Pqrs_router
from routes.video_training.sesion import sesion_router
from routes.video_training.sequence_video import sequence_video_router
from routes.video_training.video import video_router
from routes.video_training.students import student_router
from routes.contracts.contract import contract_router
from routes.permissions.permission import permission_router
from routes.app.salchigest import salchigest_router
from routes.requisitions.requisition import requisition_router
from routes.pqr.pqrs import pqr_router
from routes.cachier_money.cachier_money import cachier_money_router
from routes.Franquicias.franquicias import franquis_router
app = FastAPI()
# from routes.area import area_router
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(cachier_money_router)
app.include_router(franquis_router)
app.include_router(pqr_router)
app.include_router(requisition_router)
app.include_router(salchigest_router)
app.include_router(permission_employer_router)
app.include_router(permission_router)
app.include_router(contract_router)
app.include_router(student_router)
app.include_router(video_router)
app.include_router(sequence_video_router)
app.include_router(sesion_router)
app.include_router(recipe_data_sheet_router)
app.include_router(drive_file_router)
app.include_router(order_purchase_router)
app.include_router(contest_router)
app.include_router(daily_inventory_router)
app.include_router(monthly_inventory_router)
app.include_router(cdi_inventory_router)
app.include_router(product_router)
app.include_router(user_router)
app.include_router(ingredient_router)
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
app.include_router(work_day_router)
app.include_router(maintenance_router)
app.include_router(equipment_router)
app.include_router(recipe_router)

# app.include_router(area_router)   
app.include_router(Pqrs_router)
app.include_router(login)
# app.include_router(permission_router)
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
app.include_router(supply_router)
app.include_router(supply_delivery_router)
app.include_router(supply_delivery_item_router)
app.include_router(archivedFiles_router)
app.include_router(areas_router)
app.include_router(types_router)
app.include_router(site_schedule_router)
app.include_router(audit_router)
app.include_router(work_record_router)
app.include_router(work_shift_router)
app.include_router(shift_work_day_router)
app.include_router(shift_work_record_router)
app.include_router(shift_work_shift_router)
app.include_router(adicional_new_router)


