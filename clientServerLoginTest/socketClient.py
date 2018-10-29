#CLIENTE BASICO

import socket
import pickle
import time
print "Bienvenido cliente: "
host="localhost"
port=9999
socket1=socket.socket()
socket1.connect((host,port))
code=100
socket1.send("ESTABLISH |"+str(host)+"|"+str(port)+"|"+str(code))

def loginProcess():
	print "Iniciando proceso de login..."
	conf = "failed"
	while conf == "failed":
		user=raw_input("Ingresar Username --> ")
		contra=raw_input("Ingrese Password --> ")

		#loginCommand=raw_input("LOGIN: ")

		socket1.send(user)
		socket1.send(contra)
		#loginString= "LOG|us:"+user+"|pass:"+contra
		#socket1.send(loginCommand)
		#socket1.send(loginString)
		conf=socket1.recv(1024) #tamanio de ventana

		if (conf == "Success"):
			print "El servidor acepto los datos."
			#socket1.close()
		else:
			print "El servidor NO acepto los datos. Intente de nuevo"

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


