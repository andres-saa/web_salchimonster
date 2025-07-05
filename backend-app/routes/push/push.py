from fastapi import APIRouter
from pydantic import BaseModel
from pywebpush import webpush, WebPushException
import json
from typing import Dict
from urllib.parse import urlparse

from models.push.push import Push
push_router = APIRouter()

# 🔐 Reemplaza por tus claves reales
VAPID_PUBLIC_KEY = "BPF670w_GUT5dtXV90OZe0aB5RO1-_tzN0jaGdQu_Vv4gOWFo38s1CuCR71s_Nb1JszbmaVkYnrN1ZSLnMz6bFc"
VAPID_PRIVATE_KEY = "Lh5Rd17xWHaUaG4oxZ79ArcoZvI3h6x0tR2nTb_X5Ls"
VAPID_CLAIMS = {
    "sub": "mailto:tu-correo@ejemplo.com"
}

class Subscription(BaseModel):
    endpoint: str
    keys: dict

@push_router.post("/push/send")
def send_push(subscription: Subscription):
    payload = {
        "title": "📦 Pedido listo",
        "body": "Tu pedido ya está en camino 🚀",
    }

    try:
        webpush(
            subscription_info=subscription.dict(),
            data=json.dumps(payload),  # ✅ JSON válido
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims=VAPID_CLAIMS
        )
        return {"message": "Notificación enviada correctamente"}
    except WebPushException as e:
        return {"error": str(e)}
    
    
    
class SiteSubscription(BaseModel):
    site_id: int
    endpoint: str
    keys: Dict










push_router = APIRouter()



@push_router.post("/push/subscribe")
def subscribe_site(subscription: SiteSubscription):
    # Revisa si ya existe
    push_instance = Push()
    push_instance.create_push(subscription)
    return {"message": "Suscripción registrada"}




@push_router.post("/push/send-to-site/{site_id}")
def send_to_site(site_id: int, titulo:str = 'titulo', body:str = 'body'):
    payload = {
        "title": titulo,
        "body": body
    }

    push_instance = Push()
    subscriptions = push_instance.get_push(site_id)

    errores = []
    for sub in subscriptions:
        try:
            endpoint = sub["endpoint"]
            if not endpoint:
                raise ValueError("Endpoint vacío")

            parsed_url = urlparse(endpoint)
            if not parsed_url.scheme or not parsed_url.netloc:
                raise ValueError(f"Endpoint malformado: {endpoint}")

            audience = f"{parsed_url.scheme}://{parsed_url.netloc}"

            webpush(
                subscription_info={
                    "endpoint": endpoint,
                    "keys": sub["keys"]
                },
                data=json.dumps(payload),
                vapid_private_key=VAPID_PRIVATE_KEY,
                vapid_claims={
                    "sub": "mailto:tu-correo@ejemplo.com",
                    "aud": audience
                }
            )
        except Exception as e:
            errores.append({"endpoint": sub.get("endpoint", "desconocido"), "error": str(e)})

    return {"message": "Notificaciones enviadas", "errores": errores}



