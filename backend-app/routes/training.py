from fastapi import APIRouter
from models.training import TrainingModel
from models.assigned_attendee import AssignedAttendeeModel  # Asegúrate de importar tu modelo de Training
from models.training_attendee import TrainingAttendeeModel
from schema.training import TrainingAttendee, Training, AssignedAttendee,TrainingAttendeeList  # Importa el esquema Pydantic para trainings
from fastapi import HTTPException

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



@training_router.get("/training/{training_id}/attendees-with-status")
def get_attendees_with_status(training_id: int):
    attendee_instance = TrainingAttendeeModel()
    try:
        attendees = attendee_instance.select_attendees_with_status(training_id)
        return attendees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        attendee_instance.close_connection()




@attendee_router.post("/training/attendee")
def add_attendee_to_training(attendee: AssignedAttendee):
    attendee_instance = TrainingAttendeeModel()

    # Convertir AssignedAttendee a TrainingAttendee
    training_attendee = TrainingAttendee(
        training_id=attendee.training_id,
        attendee_id=attendee.attendee_id,
        # Aquí puedes establecer otros valores por defecto si es necesario
    )

    attendee_id = attendee_instance.insert_attendee(training_attendee)
    attendee_instance.close_connection()
    return attendee_id





@attendee_router.post("/training/attendees")
def add_attendees_to_training(attendees: TrainingAttendeeList):
    attendee_instance = TrainingAttendeeModel()
    
    # Insertar múltiples asistentes
    attendee_instance.insert_attendees(attendees.attendees)

    attendee_instance.close_connection()
    return {"message": "Attendees added successfully"}



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

@assigned_attendee_router.post("/training/assign")
def assign_attendee_to_training( attendee: AssignedAttendee):
    assigned_instance = AssignedAttendeeModel()
    # attendee_data = attendee.dict()
    # assigned_id = assigned_instance.training_id
    assigned_id = assigned_instance.insert_assigned_attendee(attendee)
    assigned_instance.close_connection()
    return assigned_id

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

    


@attendee_router.put("/training/{training_id}/attendee/{attendee_id}/mark-attendance")
def mark_attendee_attendance(training_id: int, attendee_id: int):
    attendee_instance = TrainingAttendeeModel()

    try:
        updated_attendee = attendee_instance.mark_attendance(training_id, attendee_id)
        if updated_attendee:
            return updated_attendee
        else:
            raise HTTPException(status_code=404, detail="Attendee not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        attendee_instance.close_connection()


@attendee_router.get("/attendee/{attendee_id}/invited-trainings")
def get_invited_trainings(attendee_id: int):
    attendee_instance = TrainingAttendeeModel()
    try:
        invited_trainings = attendee_instance.select_trainings_invited_to(attendee_id)
        return invited_trainings
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        attendee_instance.close_connection()


@training_router.get("/trainings/by-creator/{creator_id}")
def get_trainings_by_creator(creator_id: int):
    training_instance = TrainingModel()
    try:
        trainings = training_instance.select_trainings_by_creator_id(creator_id)
        return trainings
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        training_instance.close_connection()