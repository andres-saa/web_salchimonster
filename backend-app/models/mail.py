
import smtplib
from email.mime.text import MIMEText
from pydantic import BaseModel, EmailStr


 
def enviar_correo(destinatario, asunto, cuerpo):
    servidor_smtp = "smtp.zoho.com"
    puerto_smtp = 465  # Puerto para SSL
    usuario_smtp = "gestionhumana@salchimonster.com"  # Reemplaza con tu email de Zoho
    contraseña_smtp = "1003.Pazw"        # Reemplaza con tu contraseña de Zoho

    mensaje = MIMEText(cuerpo)
    mensaje["From"] = usuario_smtp
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto

    with smtplib.SMTP_SSL(servidor_smtp, puerto_smtp) as server:
        server.login(usuario_smtp, contraseña_smtp)
        server.sendmail(usuario_smtp, destinatario, mensaje.as_string())
