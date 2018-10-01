#CLIENTE BASICO

import socket
import pickle
import time
print "Bienvenido cliente: "
host="localhost"
port=9999
socket1=socket.socket()
socket1.connect((host,port))
socket1.send("Cliente Conectado")

def loginProcess():
	print "Iniciando proceso de login..."
	conf = "failed"
	while conf == "failed":
		user=raw_input("Ingresar Username --> ")
		contra=raw_input("Ingrese Password --> ")

		socket1.send(user)
		socket1.send(contra)
		conf=socket1.recv(1024) #tamanio de ventana

		if (conf == "Success"):
			print "El servidor acepto los datos. Cerrando la conexion.."
			#socket1.close()
		else:
			print "El servidor NO acepto los datos. Intente de nuevo"

def recibirTablero():
	print "El servidor esta enviando el tablero..."
	tablero=pickle.loads(socket1.recv(4096))
	linea=0
	while linea != 7:
		print tablero[linea]
		linea+=1
	print "Tablero Mostrado"
	print "Tipo: ",type(tablero) #esto lo ponemos para asegurarnos que nos lo envia como lista y no como string. eliminar despues
	return tablero



loginProcess()
recibirTablero()
posicion=socket1.recv(1024)
print posicion


