from pydantic import BaseModel

# Esquema para Usuarios (Opcional)
class UserSchema(BaseModel):
    username: str
    email: str
    # No incluyas la contraseña por razones de seguridad

# Esquema para Formularios
class FormSchema(BaseModel):
    title: str
    description: str
    user_id: int  # Asumiendo que asociarás un formulario con un usuario

# Esquema para Preguntas
class QuestionSchema(BaseModel):
    form_id: int
    question_text: str
    question_type: str  # Ejemplo: 'text', 'choice', 'multiple-choice'

# Esquema para Opciones de Preguntas
class QuestionOptionSchema(BaseModel):
    question_id: int
    option_text: str

# Esquema para Respuestas
class ResponseSchema(BaseModel):
    question_id: int
    user_id: int  # Opcional, si quieres asociar la respuesta con un usuario
    response: str

# Esquema para Respuestas de Múltiples Opciones
class ResponseOptionSchema(BaseModel):
    response_id: int
    option_id: int

# Puedes agregar más esquemas aquí según sea necesario
