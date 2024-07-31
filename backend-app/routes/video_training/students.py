from fastapi import APIRouter
from models.video_training.students import Student
# from schema.video_training. import student as student_schema,studentUpdate as student_update_schema
from schema.video_training.user_sequence import ReplaceUserSequencesInput

from schema.video_training.video import markVideo


student_router = APIRouter()


@student_router.get('/list-video-training-student-enrolled-by-sequence-id/{sequence_id}' , tags=['video-student -> video_student'])
def list_video_training_student( sequence_id:int):
    student_instance = Student()
    result = student_instance.get_students_enrolled_by_sequence_id(sequence_id)
    return result





@student_router.get('/list-video-mark-by-video-id/{video_id}' , tags=['video-student -> video_student'])
def list_video_training_student( video_id:int):
    student_instance = Student()
    result = student_instance.get_video_mark_users(video_id)
    return result








@student_router.get('/list-all-video-training-student-by-sequence-id/{sequence_id}' , tags=['video-student -> video_student'])
def list_video_training_student( sequence_id:int):
    student_instance = Student()
    result = student_instance.get_students_by_sequence_id(sequence_id)
    return result


@student_router.get('/list-video-training-student-enrolled-by-sequence-id-group-by-site/{sequence_id}' , tags=['video-student -> video_student'])
def list_video_training_student( sequence_id:int):
    student_instance = Student()
    result = student_instance.get_students_enrolled_by_sequence_id_group_by_site(sequence_id)
    return result

@student_router.post('/mark-video-user' , tags=['video-student -> video_student'])
def list_video_training_student( data:markVideo):
    student_instance = Student()
    result = student_instance.mark_video(data)
    return result


@student_router.get('/list-all-video-training-student-by-sequence-id-group-by-site/{sequence_id}' , tags=['video-student -> video_student'])
def list_video_training_student( sequence_id:int):
    student_instance = Student()
    result = student_instance.get_students_by_sequence_id_group_by_site(sequence_id)
    return result




@student_router.get('/list-video-training-student-enrolled-by-sequence-id-group-by-position/{sequence_id}' , tags=['video-student -> video_student'])
def list_video_training_student( sequence_id:int):
    student_instance = Student()
    result = student_instance.get_students_enrolled_by_sequence_id_group_by_position(sequence_id)
    return result



@student_router.get('/list-all-video-training-student-by-sequence-id-group-by-position/{sequence_id}' , tags=['video-student -> video_student'])
def list_video_training_student( sequence_id:int):
    student_instance = Student()
    result = student_instance.get_students_by_sequence_id_group_by_position(sequence_id)
    return result


@student_router.put('/togle_users_to_sequence_video' , tags=['video-student -> video_student'])
def list_video_training_student( data:ReplaceUserSequencesInput):
    student_instance = Student()
    result = student_instance.replace_user_sequences(data)
    return result






# @student_router.post('/insert-video-training-student' , tags=['video-student -> video_student'])
# def insert_video_training_student(data:student_schema):
#     student_instance = student()
#     result = student_instance.insert_student(data)
#     return result

# @student_router.delete('/delete-video-training-student/{student_id}' , tags=['video-student -> video_student'])
# def delete_video_training_student(student_id:int):
#     student_instance = student()
#     result = student_instance.delete_student(student_id)
#     return result


# @student_router.put('/update-video-training-student/{student_id}' , tags=['video-student -> video_student'])
# def update_video_training_student(data:student_update_schema, student_id:int):
#     student_instance = student()
#     result = student_instance.update_student(student_id,data)
#     return result
