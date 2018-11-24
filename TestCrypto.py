import SocketServer
import time
import threading
import pickle
from Crypto import Random
from Crypto.Cipher import AES
import base64


BLOCK_SIZE=32

def encrypt(message, passphrase):
    # passphrase MUST be 16, 24 or 32 bytes long, how can I do that ?
    print "Encriptando... <<" + message + ">>"
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    encriptado = base64.b64encode(aes.encrypt(message))
    print "Encriptado <<" + encriptado + ">>"
    return encriptado

def decrypt(encrypted, passphrase):
    print "Desencriptando... <<" + encrypted + ">>"
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    desencriptado = aes.decrypt(base64.b64decode(encrypted))
    print "Desencriptado <<" + desencriptado + ">>"
    return desencriptado

def main():
    a = encrypt("hola", "asd")
    b = decrypt(a, "asd")

    c = raw_input("enter pa salir")

main()
