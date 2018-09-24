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

def recibirTablero(matriz):
	print "El servidor esta enviando el tablero..."
	print "hace falta programar esta parte"



loginProcess()
ancho, alto = 11, 7;
Matriz = [[0 for x in range(ancho)] for y in range(alto)]
recibirTablero(Matriz)
