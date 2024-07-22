from fastapi import APIRouter
from models.video_training.sesion import Sesion
from schema.video_training.sesion import Sesion as sesion_schema,SesionUpdate as sesion_update_schema





sesion_router = APIRouter()


@sesion_router.get('/list-video-training-sesion' , tags=['video-sesion -> video_sesion'])
def list_video_training_sesion():
    sesion_instance = Sesion()
    result = sesion_instance.get_all_sesion()
    return result



@sesion_router.post('/insert-video-training-sesion' , tags=['video-sesion -> video_sesion'])
def insert_video_training_sesion(data:sesion_schema):
    sesion_instance = Sesion()
    result = sesion_instance.insert_sesion(data)
    return result

@sesion_router.delete('/delete-video-training-sesion/{sesion_id}' , tags=['video-sesion -> video_sesion'])
def delete_video_training_sesion(sesion_id:int):
    sesion_instance = Sesion()
    result = sesion_instance.delete_sesion(sesion_id)
    return result


@sesion_router.put('/update-video-training-sesion/{sesion_id}' , tags=['video-sesion -> video_sesion'])
def update_video_training_sesion(data:sesion_update_schema, sesion_id:int):
    sesion_instance = Sesion()
    result = sesion_instance.update_sesion(sesion_id,data)
    return result
