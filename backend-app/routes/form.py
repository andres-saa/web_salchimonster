from fastapi import APIRouter
from models.form import FormManager
from schema.form import FormSchema, QuestionSchema, QuestionOptionSchema, ResponseSchema

form_router = APIRouter()

@form_router.get("/forms")
def get_forms():
    form_instance = FormManager()
    forms = form_instance.get_all_forms()
    form_instance.close_connection()
    return forms

@form_router.get("/form/{form_id}")
def get_form_by_id(form_id: int):
    form_instance = FormManager()
    form = form_instance.get_form_by_id(form_id)
    form_instance.close_connection()
    return form

@form_router.get("/form/{form_id}/questions")
def get_questions_by_form_id(form_id: int):
    form_instance = FormManager()
    questions = form_instance.get_questions_by_form_id(form_id)
    form_instance.close_connection()
    return questions

@form_router.get("/question/{question_id}/options")
def get_question_options_by_question_id(question_id: int):
    form_instance = FormManager()
    options = form_instance.get_question_options_by_question_id(question_id)
    form_instance.close_connection()
    return options

@form_router.get("/question/{question_id}/responses")
def get_responses_by_question_id(question_id: int):
    form_instance = FormManager()
    responses = form_instance.get_responses_by_question_id(question_id)
    form_instance.close_connection()
    return responses

@form_router.post("/form")
def create_form(form: FormSchema):
    form_instance = FormManager()
    form_id = form_instance.insert_form(form)
    form_instance.close_connection()
    return {"form_id": form_id}

@form_router.post("/question")
def create_question(question: QuestionSchema):
    form_instance = FormManager()
    question_id = form_instance.insert_question(question)
    form_instance.close_connection()
    return {"question_id": question_id}

@form_router.post("/question_option")
def create_question_option(option: QuestionOptionSchema):
    form_instance = FormManager()
    option_id = form_instance.insert_question_option(option)
    form_instance.close_connection()
    return {"option_id": option_id}

@form_router.post("/response")
def create_response(response: ResponseSchema):
    form_instance = FormManager()
    response_id = form_instance.insert_response(response)
    form_instance.close_connection()
    return {"response_id": response_id}

@form_router.put("/form/{form_id}")
def update_form(form_id: int, updated_form: FormSchema):
    form_instance = FormManager()
    updated_form_data = form_instance.update_form(form_id, updated_form)

    if updated_form_data:
        form_instance.close_connection()
        return updated_form_data
    else:
        form_instance.close_connection()
        return {"message": "Form not found"}

# Puedes agregar aquí métodos PUT para preguntas, opciones de preguntas y respuestas si lo necesitas

# ... otros métodos HTTP (DELETE, etc.) según sea necesario
