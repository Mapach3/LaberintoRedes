#CLIENTE BASICO

import socket
import pickle
import time
print "Bienvenido cliente: "
host = "localhost"
port = 9999
socket1=socket.socket()
socket1.connect((host,port))
code=100
socket1.send("ESTABLISH |"+str(host)+"|"+str(port)+"|"+str(code))

def loginProcess():
	print "Iniciando proceso de login..."
	estado_respuesta = ""
	while estado_respuesta != "OK":
		time.sleep(0.1)
		user=raw_input("Ingresar Username --> ")
		contra=raw_input("Ingrese Password --> ")
		socket1.send("LOG|user:" + user + "|pass:" + contra)
		respuesta = socket1.recv(1024) #tamanio de ventana
		respuesta_split = respuesta.split("|")
		tipo_comando = respuesta_split[0]
		codigo_respuesta = respuesta_split[1]
		print str(codigo_respuesta)
		estado_respuesta = respuesta_split[2]
		print estado_respuesta
		if (estado_respuesta == "OK"):
			print "El servidor acepto los datos."
		else:
			print "El servidor NO acepto los datos. Intente de nuevo"
	recibirTablero()
	tipo_respuesta = ""
	while tipo_respuesta != "WIN":
		direccion = raw_input("Moverse para --> ")
		socket1.send("MOV|direccion:" + direccion)
		respuesta = socket1.recv(1024)
		respuesta_split = respuesta.split("|")
		tipo_respuesta = respuesta_split[0]
		descripcion_respuesta_split = respuesta_split[1].split(":")
		descripcion_respuesta = descripcion_respuesta_split[1]
		print descripcion_respuesta
		recibirTablero()


	print "has salido"

def recibirTablero():
	print "El servidor esta enviando el tablero..."
	tablero=pickle.loads(socket1.recv(1024))
	linea=0
	while linea != 4:
		print tablero[linea]
		linea+=1
	print "Tablero Mostrado"
	#print "Tipo: ",type(tablero) #esto lo ponemos para asegurarnos que nos lo envia como lista y no como string. eliminar despues
	return tablero



loginProcess()
recibirTablero()
posicion=socket1.recv(1024)
print posicion
