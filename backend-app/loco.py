from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Configurar Chrome para que funcione en modo headless
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Ejecuta Chrome en modo headless
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Ruta al ChromeDriver
service = Service('E:/path/to/chromedriver')

# Inicializar el WebDriver con el servicio
driver = webdriver.Chrome(service=service, options=options)

# Navegar a Google
driver.get('https://www.google.com')

# Esperar un momento para asegurarse de que la página se cargue completamente
time.sleep(5)

# Obtener el contenido de la página
page_content = driver.page_source

# Guardar el contenido en un archivo local
with open('google_page.html', 'w', encoding='utf-8') as file:
    file.write(page_content)

# Finalizar el navegador
driver.quit()
