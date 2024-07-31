from fastapi import APIRouter,Depends

from schema.video_training.video import Video as video_schema, VideoPost as video_post_schema, VideoUpdate as video_update_schema
from models.video_training.video import Video


from auth_utils.Security import security

video_router = APIRouter()


@video_router.get( '/list-video' , tags=[ 'video_training -> video' ] )
def list_video_training_video():
    video_instance = Video()
    result = video_instance.get_all_video()
    return result   


@video_router.get( '/list-video-by-sequence-id/{sequence_id}' , tags=[ 'video_training -> video' ] )
def list_video_training_video_by_sesion_id( sequence_id:int):
    video_instance = Video()
    result = video_instance.get_video_by_sequence_id(sequence_id)
    return result



@video_router.get( '/list-video-by-sequence-id-and-student-id/{sequence_id}/{student_id}' , tags=[ 'video_training -> video' ] )
def list_video_training_video_by_sesion_id( sequence_id:int, student_id:int):
    video_instance = Video()
    result = video_instance.get_video_by_sequence_id_and_student_id(sequence_id,student_id)
    return result




@video_router.post( '/insert-video-training' , tags=[ 'video_training -> video' ] )
def insert_video_training_video(data:video_post_schema):
    video_instance = Video()
    result = video_instance.insert_video(data)
    return result

@video_router.delete( '/delete-video-training/{video_id}' , tags=[ 'video_training -> video' ])
def delete_video_training_video(video_id:int):
    video_instance = Video()
    result = video_instance.delete_video(video_id)
    return result

@video_router.put( '/update-video-training/{video_id}' , tags=[ 'video_training -> video' ])
def update_video_training_video( data:video_update_schema, video_id:int ):
    video_instance = Video()
    result = video_instance.update_video( video_id,data )
    return result
