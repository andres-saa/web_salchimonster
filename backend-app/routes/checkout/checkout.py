from fastapi import FastAPI, Request, status, APIRouter
from fastapi.responses import JSONResponse
from models.orders.order2 import Order2
import hashlib

app = FastAPI()

# Datos de configuración (ejemplo)
P_CUST_ID_CLIENTE = "1549908"  # p_cust_id_cliente de tu cuenta Epayco
P_KEY = "e9798eef6938e388bab95d14314243f85f6c3e7a"              # p_key de tu cuenta Epayco

# Simulación de valores internos en el comercio
NUM_ORDER = "DIS-0194"      # Número de orden real que espera tu sistema
VALUE_ORDER = "146850"   # Valor esperado para esa orden

checkout_router = APIRouter()

@checkout_router.post("/confirmacion-epayco")
async def confirmacion_epayco(request: Request):
    """
    Recibe y valida la confirmación de pago de Epayco.
    Lee parámetros desde la query (URL) porque Epayco
    suele enviarlos así incluso en un POST.
    """
    data = request.query_params

    # 1) Extraer datos enviados por Epayco
    x_ref_payco       = data.get("x_ref_payco")
    x_transaction_id  = data.get("x_transaction_id")
    x_amount          = data.get("x_amount")
    x_currency_code   = data.get("x_currency_code")
    x_signature       = data.get("x_signature")
    x_id_invoice      = data.get("x_id_invoice")
    x_response        = data.get("x_response")               # "Aceptada", "Rechazada", etc.
    x_motivo          = data.get("x_response_reason_text")   # Texto con mayor detalle
    x_autorizacion    = data.get("x_approval_code")          # Ejemplo: "000000"
    x_cod_response    = data.get("x_cod_response")
    id_factura        = data.get("x_id_invoice")
    
    # 1 = aceptada, 2 = rechazada, etc.

    order_instance = Order2()
    
    real_order = order_instance.get_order_status_by_order_id(id_factura)

    valor_real = real_order['pe_json']['delivery']['delivery_pagocon']
    
    print(valor_real)
    print(x_amount)
    # 2) Calcular la firma local para comparar
    #    La concatenación y orden debe coincidir con la documentación de Epayco
    #    PHP: hash('sha256', p_cust_id_cliente ^ p_key ^ x_ref_payco ^ x_transaction_id ^ x_amount ^ x_currency_code)
    to_sign = f"{P_CUST_ID_CLIENTE}^{P_KEY}^{x_ref_payco}^{x_transaction_id}^{x_amount}^{x_currency_code}"
    computed_signature = hashlib.sha256(to_sign.encode('utf-8')).hexdigest()

    # 3) Validar número de orden y valor (según tu lógica interna)
    if (x_id_invoice == id_factura and str(float(x_amount)) == str(float(valor_real))):
        # 4) Validar la firma
        if x_signature == computed_signature:
            # Firma válida, revisar el estado de la transacción
            if x_cod_response == "1":
                # Transacción aceptada
                
                print('aprobada')
                order_instance.pay_order(id_factura,x_ref_payco)
                return {"message": "Transacción aceptada con éxito"}
            
            elif x_cod_response == "2":
                # Transacción rechazada
                print('recgazada')
                return {"message": "Transacción rechazada"}
            elif x_cod_response == "3":
                # Transacción pendiente
                print('pendiente')

                return {"message": "Transacción pendiente"}
            elif x_cod_response == "4":
                # Transacción fallida
                print('fallida')

                return {"message": "Transacción fallida"}
            else:
                # Caso no definido explícitamente
                return {
                    "message": f"Transacción con estado desconocido: {x_cod_response}"
                }
        else:
            # Firma incorrecta
            return JSONResponse(
                content={"error": "Firma no válida"},
                status_code=status.HTTP_400_BAD_REQUEST
            )
    else:
        # Orden o valor no coinciden con lo esperado en tu sistema
        return JSONResponse(
            content={"error": "Número de orden o valor pagado no coinciden"},
            status_code=status.HTTP_400_BAD_REQUEST
        )
