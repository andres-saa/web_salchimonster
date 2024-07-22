from fastapi import APIRouter
from models.video_training.sesion import Sesion


video_training_router = APIRouter()


@video_training_router.get("Hola")
def hola():
    return 'hola'