import requests

def enviar_mensaje_whatsapp(api_key, source_number, destination_number, message, source_name):
    """
    Envia un mensaje de WhatsApp usando la API de Gupshup.

    Parámetros:
    - api_key (str): La clave de API proporcionada por Gupshup.
    - source_number (str): El número de teléfono del remitente.
    - destination_number (str): El número de teléfono del destinatario.
    - message (str): El mensaje de texto a enviar.
    - source_name (str): El nombre del remitente.
    """
    url = "https://api.gupshup.io/wa/api/v1/msg"
    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',
        'apikey': api_key,
    }
    data = {
        'channel': 'whatsapp',
        'source': source_number,
        'destination': destination_number,
        'message': f'{{"type":"text","text":"{message}"}}',
        'src.name': source_name
    }

    response = requests.post(url, headers=headers, data=data)
    return response.text