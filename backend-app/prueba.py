import requests

def enviar_mensaje_template(destino):
    url = "https://api.gupshup.io/wa/api/v1/template/msg"
    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'apikey': 'obg0iystmnq4v0ln4r5fnjcvankhtjp0',
        'cache-control': 'no-cache'
    }
    # Preparar los parámetros del template
    params = ["Bryan", "SalchiGest", "150.000", "150.000", "150.000", "150.000", "150.000", "150.000", "150.000", "150.000", "150.000", "150.000"]
    data = {
        'channel': 'whatsapp',
        'source': '573053447255',
        'destination': destino,
        'src.name': 'Salchimonster',
        'template': '{"id":"03930a95-275d-42c1-b295-72a6d364666b","params":' + str(params) + '}'
    }
    # Convertir la lista params a formato JSON adecuado para la URL
    data['template'] = data['template'].replace("'", '"')

    response = requests.post(url, headers=headers, data=data)
    return response.text

# Llamar a la función con un número de teléfono de destino
respuesta = enviar_mensaje_template('573226892988')
print(respuesta)
