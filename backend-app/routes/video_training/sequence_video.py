from fastapi import APIRouter

from schema.video_training.sequence_video import SequenceVideoPost as sequence_video_schema,SequenceVideoUpdate as sequence_video_update_schema
from models.video_training.sequence_video import SequenceVideo




sequence_video_router = APIRouter()


@sequence_video_router.get( '/list-video-training-sequence-video' , tags=[ 'video_training -> video_sequence' ] )
def list_video_training_sequence_video():
    sequence_video_instance = SequenceVideo()
    result = sequence_video_instance.get_all_sequence_video()
    return result


@sequence_video_router.get( '/list-video-training-sequence-video-by-sesion-id/{sesion_id}' , tags=[ 'video_training -> video_sequence' ] )
def list_video_training_sequence_video_by_sesion_id( sesion_id:int):
    sequence_video_instance = SequenceVideo()
    result = sequence_video_instance.get_sequence_video_by_sesion_id(sesion_id)
    return result



@sequence_video_router.get( '/list-video-training-sequence-video-by-student-id/{student_id}' , tags=[ 'video_training -> video_sequence' ] )
def list_video_training_sequence_video_by_sesion_id( student_id:int):
    sequence_video_instance = SequenceVideo()
    result = sequence_video_instance.get_sequence_video_by_student_id(student_id)
    return result





@sequence_video_router.post( '/insert-video-training-sequence' , tags=[ 'video_training -> video_sequence' ] )
def insert_video_training_sequence_video(data:sequence_video_schema):
    sequence_video_instance = SequenceVideo()
    result = sequence_video_instance.insert_sequence_video(data)
    return result

@sequence_video_router.delete( '/delete-video-training-sequence/{sequence_video_id}' , tags=[ 'video_training -> video_sequence' ])
def delete_video_training_sequence_video(sequence_video_id:int):
    sequence_video_instance = SequenceVideo()
    result = sequence_video_instance.delete_sequence_video(sequence_video_id)
    return result

@sequence_video_router.put( '/update-video-training-sequence-video/{sequence_video_id}' , tags=[ 'video_training -> video_sequence' ])
def update_video_training_sequence_video( data:sequence_video_update_schema, sequence_video_id:int ):
    sequence_video_instance = SequenceVideo()
    result = sequence_video_instance.update_sequence_video( sequence_video_id,data )
    return result
