from django.db import models

from Crypto.Cipher import AESpip
from Crypto.Protocol.KDF import PBKDF2


class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=3)
    marja = models.DecimalField(max_digits=10, decimal_places=3)
    package_code = models.CharField(max_length=100)

    def encrypt_field(self, field_value):
        key = PBKDF2(settings.SECRET_KEY.encode(), b'salt', dkLen=32)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(field_value.encode())
        return ciphertext.hex()

    def decrypt_field(self, encrypted_value):
        key = PBKDF2(settings.SECRET_KEY.encode(), b'salt', dkLen=32)
        cipher = AES.new(key, AES.MODE_EAX)
        decrypted_value = cipher.decrypt(bytes.fromhex(encrypted_value))
        return decrypted_value.decode()
