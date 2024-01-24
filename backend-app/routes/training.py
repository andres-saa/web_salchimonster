from fastapi import APIRouter
from models.training import TrainingModel
from models.assigned_attendee import AssignedAttendeeModel  # Asegúrate de importar tu modelo de Training
from models.training_attendee import TrainingAttendeeModel
from schema.training import TrainingAttendee, Training, AssignedAttendee  # Importa el esquema Pydantic para trainings

training_router = APIRouter()

@training_router.get("/trainings")
def get_trainings():
    training_instance = TrainingModel()
    trainings = training_instance.select_all_trainings()
    training_instance.close_connection()
    return trainings

@training_router.get("/training/{training_id}")
def get_training_by_id(training_id: int):
    training_instance = TrainingModel()
    training = training_instance.select_training_by_id(training_id)
    training_instance.close_connection()
    return training

@training_router.delete("/training/{training_id}")
def delete_training(training_id: int):
    training_instance = TrainingModel()
    result = training_instance.delete_training(training_id)
    training_instance.close_connection()
    return {"message": result}

@training_router.post("/training")
def create_training(training: Training):
    training_instance = TrainingModel()
    training_id = training_instance.insert_training(training)
    training_instance.close_connection()
    return {"training_id": training_id}

@training_router.put("/training/{training_id}")
def update_training(training_id: int, updated_training: Training):
    training_instance = TrainingModel()
    updated_training_data = training_instance.update_training(training_id, updated_training)

    if updated_training_data:
        training_instance.close_connection()
        return updated_training_data
    else:
        training_instance.close_connection()
        return {"message": "Training not found"}


attendee_router = APIRouter()

@attendee_router.get("/training/{training_id}/attendees")
def get_training_attendees(training_id: int):
    attendee_instance = TrainingAttendeeModel()
    attendees = attendee_instance.select_all_attendees_for_training(training_id)
    attendee_instance.close_connection()
    return attendees

@attendee_router.post("/training/{training_id}/attendee")
def add_attendee_to_training(training_id: int, attendee: AssignedAttendee):
    attendee_instance = TrainingAttendeeModel()
    attendee_data = attendee.dict()
    attendee_data["training_id"] = training_id  # Asegúrate de incluir el training_id en los datos del asistente
    attendee_id = attendee_instance.insert_attendee(attendee_data)
    attendee_instance.close_connection()
    return {"attendee_id": attendee_id}

@attendee_router.delete("/training/{training_id}/attendee/{attendee_id}")
def remove_attendee_from_training(training_id: int, attendee_id: int):
    attendee_instance = TrainingAttendeeModel()
    result = attendee_instance.delete_attendee(training_id, attendee_id)
    attendee_instance.close_connection()
    return {"message": result}

@attendee_router.get("/training/{training_id}/attendee/{attendee_id}")
def get_attendee(training_id: int, attendee_id: int):
    attendee_instance = TrainingAttendeeModel()
    attendee = attendee_instance.select_attendee_by_id(training_id, attendee_id)
    attendee_instance.close_connection()
    if attendee:
        return attendee
    else:
        return {"error": "Attendee not found"}

assigned_attendee_router = APIRouter()


@assigned_attendee_router.get("/training/{training_id}/assigned")
def get_assigned_attendees(training_id: int):
    assigned_instance = AssignedAttendeeModel()
    assigned_attendees = assigned_instance.select_all_assigned_for_training(training_id)
    assigned_instance.close_connection()
    return assigned_attendees

@assigned_attendee_router.post("/training/{training_id}/assign")
def assign_attendee_to_training(training_id: int, attendee: AssignedAttendee):
    assigned_instance = AssignedAttendeeModel()
    attendee_data = attendee.dict()
    attendee_data["training_id"] = training_id
    assigned_id = assigned_instance.insert_assigned_attendee(attendee_data)
    assigned_instance.close_connection()
    return {"assigned_id": assigned_id}

@assigned_attendee_router.get("/training/{training_id}/assigned/{attendee_id}")
def get_assigned_attendee(training_id: int, attendee_id: int):
    assigned_instance = AssignedAttendeeModel()
    attendee = assigned_instance.select_assigned_attendee_by_id(training_id, attendee_id)
    assigned_instance.close_connection()
    if attendee:
        return attendee
    else:
        return {"error": "Assigned attendee not found"}


@assigned_attendee_router.delete("/training/{training_id}/unassign/{attendee_id}")
def unassign_attendee_from_training(training_id: int, attendee_id: int):
    assigned_instance = AssignedAttendeeModel()
    result = assigned_instance.delete_assigned_attendee(training_id, attendee_id)
    assigned_instance.close_connection()
    return {"message": result}

    