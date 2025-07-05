from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import base64

# Generar claves
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# Obtener el número privado
private_value = private_key.private_numbers().private_value
private_bytes = private_value.to_bytes(32, byteorder="big")
vapid_private_key = base64.urlsafe_b64encode(private_bytes).decode("utf-8").rstrip("=")

# Obtener los números públicos
public_numbers = public_key.public_numbers()
x = public_numbers.x.to_bytes(32, byteorder="big")
y = public_numbers.y.to_bytes(32, byteorder="big")
uncompressed_key = b'\x04' + x + y
vapid_public_key = base64.urlsafe_b64encode(uncompressed_key).decode("utf-8").rstrip("=")

print("🔐 VAPID Public Key:\n", vapid_public_key)
print("\n🔐 VAPID Private Key:\n", vapid_private_key)
