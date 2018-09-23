#CLIENTE BASICO

import socket
print "Bienvenido cliente: "
host="localhost"
port=9999
socket1=socket.socket()
socket1.connect((host,port))
socket1.send("Cliente Conectado")

def loginProcess():
	print "Iniciando proceso de login..."
	conf = "failed"
	while True:
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


loginProcess()
