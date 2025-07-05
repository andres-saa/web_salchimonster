from fastapi import FastAPI, Request, status, APIRouter
from fastapi.responses import JSONResponse
from models.orders.order2 import Order2
import hashlib
import os
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("epayco")

app = FastAPI()
checkout_router = APIRouter()

# Variables de entorno (usa un archivo .env o configuración del sistema)
P_CUST_ID_CLIENTE = os.getenv("EPAYCO_CLIENT_ID")
P_KEY = os.getenv("EPAYCO_SECRET_KEY")

P_CUST_ID_CLIENTE_SALCHI = os.getenv("EPAYCO_SALCHI_CLIENT_ID")
P_KEY_SALCHI             = os.getenv("EPAYCO_SALCHI_SECRET_KEY")

P_CUST_ID_CLIENTE_DISTRI = os.getenv("EPAYCO_DISTRI_CLIENT_ID")
P_KEY_DISTRI             = os.getenv("EPAYCO_DISTRI_SECRET_KEY")



@checkout_router.post("/confirmacion-epayco")
async def confirmacion_epayco(request: Request):
    """
    Recibe y valida la confirmación de pago de Epayco.
    Lee parámetros desde la query (URL) porque Epayco suele enviarlos así incluso en un POST.
    """
    try:
        data = request.query_params

        # Extraer campos necesarios
        x_ref_payco = data.get("x_ref_payco")
        x_transaction_id = data.get("x_transaction_id")
        x_amount = data.get("x_amount")
        x_currency_code = data.get("x_currency_code")
        x_signature = data.get("x_signature")
        x_id_invoice = data.get("x_id_invoice")
        x_response = data.get("x_response")
        x_motivo = data.get("x_response_reason_text")
        x_autorizacion = data.get("x_approval_code")
        x_cod_response = data.get("x_cod_response")
        id_factura = x_id_invoice

        # Validación de campos esenciales
        if not all([x_ref_payco, x_transaction_id, x_amount, x_currency_code, x_signature, x_id_invoice]):
            return JSONResponse(
                content={"error": "Parámetros incompletos en la confirmación"},
                status_code=status.HTTP_400_BAD_REQUEST
            )

        # Buscar orden en el sistema
        order_instance = Order2()
        real_order = order_instance.get_order_status_by_order_id(id_factura)

        if not real_order or 'pe_json' not in real_order or 'delivery' not in real_order['pe_json']:
            return JSONResponse(
                content={"error": "Orden no encontrada o formato inválido"},
                status_code=status.HTTP_404_NOT_FOUND
            )

        valor_real = real_order['pe_json']['delivery']['delivery_pagocon']
        
        
        cust_id = ''
        p_key = ''
        
        if x_id_invoice.upper().startswith("DIS"):
            cust_id = P_CUST_ID_CLIENTE_DISTRI
            p_key   = P_KEY_DISTRI
        else:
            cust_id = P_CUST_ID_CLIENTE_SALCHI
            p_key   = P_KEY_SALCHI

        # Firma local
        to_sign = f"{cust_id}^{p_key}^{x_ref_payco}^{x_transaction_id}^{x_amount}^{x_currency_code}"
        computed_signature = hashlib.sha256(to_sign.encode('utf-8')).hexdigest()

        # Función para comparar floats con tolerancia
        def floats_approx_equal(a, b, epsilon=0.01):
            return abs(float(a) - float(b)) < epsilon

        if x_id_invoice == id_factura and floats_approx_equal(x_amount, valor_real):
            if x_signature == computed_signature:
                # Firma válida, revisar estado de transacción
                if x_cod_response == "1":
                    logger.info(f"Transacción aprobada: {id_factura}")
                    order_instance.pay_order(id_factura, x_ref_payco)
                    return {"message": "Transacción aceptada con éxito"}

                elif x_cod_response == "2":
                    logger.warning(f"Transacción rechazada: {id_factura}")
                    return {"message": "Transacción rechazada"}

                elif x_cod_response == "3":
                    logger.info(f"Transacción pendiente: {id_factura}")
                    return {"message": "Transacción pendiente"}

                elif x_cod_response == "4":
                    logger.error(f"Transacción fallida: {id_factura}")
                    return {"message": "Transacción fallida"}

                else:
                    logger.warning(f"Transacción con estado desconocido: {x_cod_response}")
                    return {"message": f"Transacción con estado desconocido: {x_cod_response}"}
            else:
                logger.warning("Firma no válida")
                return JSONResponse(
                    content={"error": "Firma no válida"},
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        else:
            logger.warning("Número de orden o valor pagado no coinciden")
            return JSONResponse(
                content={"error": "Número de orden o valor pagado no coinciden"},
                status_code=status.HTTP_400_BAD_REQUEST
            )

    except Exception as e:
        logger.exception("Error procesando la confirmación de Epayco")
        return JSONResponse(
            content={"error": "Error interno procesando la confirmación"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# Registrar el router en la app principal
app.include_router(checkout_router)
