import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def derive_key_from_password(password: str):
    password = bytes(password, "UTF-8")
    # Generate a key from the password and salt using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=bytes(31),
        iterations=600000,  # 600k is pretty secure
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key


class EncryptionEngine:

    @staticmethod
    def encrypt(entry: str, password: str) -> str:
        fernet = Fernet(derive_key_from_password(password))
        encrypted_entry = fernet.encrypt(entry.encode('UTF-8'))
        return encrypted_entry.decode("UTF-8")

    @staticmethod
    def decrypt(entry: str, password: str):
        fernet = Fernet(derive_key_from_password(password))
        return fernet.decrypt(entry.encode("UTF-8")).decode()
