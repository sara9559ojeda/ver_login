from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import os
import base64

# Clave secreta obtenida desde las variables de entorno (similar a process.env.AUTH_AES_SECRET_KEY en Node.js)
secret_key = os.getenv('AUTH_AES_SECRET_KEY')

def get_key_iv():
    # Deriva una clave y un vector de inicialización (IV) desde la clave secreta
    key = PBKDF2(secret_key, b'salt', dkLen=32)  # Usa salt para derivar la clave (puede cambiarse a otro valor)
    iv = b'\x00' * 16  # IV fijo (puedes cambiar esto para tener un IV único)
    return key, iv

def encrypt(data):
    key, iv = get_key_iv()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt(data):
    key, iv = get_key_iv()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(base64.b64decode(data)), AES.block_size)
    return decrypted_data.decode('utf-8')