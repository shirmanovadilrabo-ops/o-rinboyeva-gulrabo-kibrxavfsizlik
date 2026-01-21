# signer.py
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64

# Xususiy kalitni o‘qish
with open("private.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

message = b"gul"

# Imzo yaratish (RSA-PSS + SHA256)
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Xabar:", message.decode())
print("Imzo (Base64):", base64.b64encode(signature).decode())