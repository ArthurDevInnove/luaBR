from dotenv import load_dotenv
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

load_dotenv()

key_64 = os.getenv("KEY_64")
key = bytes.fromhex(key_64)
iv = os.getenv("IV")
iv = bytes.fromhex(iv)


def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    parsed_data = pad(data.encode("utf-8"), AES.block_size)
    encrypted_data = cipher.encrypt(parsed_data)
    return base64.b64encode(encrypted_data).decode("utf-8")


def uncrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = base64.b64decode(data)
    padded_message = cipher.decrypt(encrypted)
    return unpad(padded_message, AES.block_size).decode("utf-8")