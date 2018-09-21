#CLIENTE BASICO

import socket
print "Prueba del Login del cliente"
host="localhost"
port=9999
socket1=socket.socket()
socket1.connect((host,port))

while True:
	user=raw_input("Ingresar Username --> ")
	contra=raw_input("Ingrese Password --> ")

	socket1.send(user)
	socket1.send(contra)
	conf=socket1.recv(1024) #tamanio de ventana

	if (conf == "Success"):
		print "El servidor acepto los datos. Cerrando la conexion.."
		break
		socket1.close()
	else:
		print "El servidor NO acepto los datos."
