from fastapi import FastAPI, Request, status,APIRouter
from fastapi.responses import JSONResponse
import hashlib

checkout_router = APIRouter()

# Reemplaza con tu llave privada real
PRIVATE_KEY = "fb76335ee644e3d9cd90a67f7196018e"

@checkout_router.get("/")
def read_root():
    return {"message": "Bienvenido a mi API con FastAPI y Epayco"}

@checkout_router.post("/confirmacion-epayco")
async def confirmacion_epayco(request: Request):
    """
    Endpoint para recibir la confirmación de pago de Epayco.
    Epayco usualmente envía los datos via form-data (x-www-form-urlencoded).
    """
    form_data = await request.form()

    # Extraer parámetros relevantes
    x_signature = form_data.get("x_signature")
    x_cod_transaction_state = form_data.get("x_cod_transaction_state")
    x_ref_payco = form_data.get("x_ref_payco")
    x_transaction_id = form_data.get("x_transaction_id")
    x_amount = form_data.get("x_amount")

    # Recalcular la firma para verificar la autenticidad
    # (la concatenación y el orden dependen de la documentación oficial de Epayco)
    # Firma típica:  x_ref_payco ^ x_transaction_id ^ x_amount ^ x_cod_transaction_state ^ PRIVATE_KEY

    signature_to_check_string = f"{x_ref_payco}^{x_transaction_id}^{x_amount}^{x_cod_transaction_state}^{PRIVATE_KEY}"
    signature_to_check = hashlib.sha256(signature_to_check_string.encode('utf-8')).hexdigest()

    if x_signature == signature_to_check:
        # Firma válida; validamos el estado de la transacción
        if x_cod_transaction_state == "1":
            # Pago exitoso
            # Aquí puedes actualizar tu base de datos, enviar correos, etc.
            print("Pago exitoso. Ref:", x_ref_payco)
            return JSONResponse(
                content={"message": "Pago exitoso", "ref_payco": x_ref_payco},
                status_code=status.HTTP_200_OK
            )
        else:
            # Pago rechazado u otro estado
            print("Pago no exitoso. Estado:", x_cod_transaction_state)
            return JSONResponse(
                content={"message": "Pago no exitoso", "estado": x_cod_transaction_state},
                status_code=status.HTTP_200_OK
            )
    else:
        # Firma no válida: podría ser un intento de fraude o datos manipulados
        print("Firma inválida, posible fraude. Data recibida:", form_data)
        return JSONResponse(
            content={"message": "Firma inválida"},
            status_code=status.HTTP_400_BAD_REQUEST
        )
