
# Diccionario para los colores de las bandas
colores = {
    "negro": 0, "marron": 1, "rojo": 2, "naranja": 3, "amarillo": 4,
    "verde": 5, "azul": 6, "violeta": 7, "gris": 8, "blanco": 9
}

# Diccionario para los multiplicadores
multiplicadores = {
    "negro": 1, "marron": 10, "rojo": 100, "naranja": 1000, "amarillo": 10000,
    "verde": 100000, "azul": 1000000, "violeta": 10000000, "gris": 100000000, "blanco": 1000000000,
    "dorado": 0.1, "plateado": 0.01
}

# Diccionario para la tolerancia
tolerancias = {
    "marron": "±1%", "rojo": "±2%", "dorado": "±5%", "plateado": "±10%", "sin color": "±20%"
}

def calcular_valor_resistencia(bandas):
    try:
        # Extraer los colores individuales de las bandas
        color1, color2, color_multiplicador, color_tolerancia = bandas
        
        # Calcular los dos primeros dígitos
        primer_digito = colores[color1]
        segundo_digito = colores[color2]
        
        # Calcular el valor de la resistencia
        valor_resistencia = (primer_digito * 10 + segundo_digito) * multiplicadores[color_multiplicador]
        
        # Obtener la tolerancia
        tolerancia = tolerancias[color_tolerancia]
        
        return f"Valor de la resistencia: {valor_resistencia} ohmios, Tolerancia: {tolerancia}"
    except KeyError:
        return "Uno de los colores ingresados no es válido. Por favor, verifica e intenta nuevamente."

# Solicitar al usuario que ingrese los colores de las bandas
print("Introduce los colores de las cuatro bandas de la resistencia.")
color1 = input("Color de la primera banda: ").strip().lower()
color2 = input("Color de la segunda banda: ").strip().lower()
color_multiplicador = input("Color de la tercera banda (multiplicador): ").strip().lower()
color_tolerancia = input("Color de la cuarta banda (tolerancia): ").strip().lower()

# Calcular y mostrar el resultado
resultado = calcular_valor_resistencia([color1, color2, color_multiplicador, color_tolerancia])
print(resultado)
