# verifier.py
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64

# Ochiq kalitni o‘qish
with open("public.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

message = b"gul"

# Imzoni bu yerga qo'yasiz (Base64 ko‘rinishda)
signature_b64 = input("Imzoni (Base64) kiriting: ")
signature = base64.b64decode(signature_b64)

# Imzoni tekshirish
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✔️ Imzo to‘g‘ri!")
except Exception:
    print("❌ Imzo noto‘g‘ri!")