##SERVIDOR##
import SocketServer
import time
import pickle

class miTcpHandler(SocketServer.BaseRequestHandler):		#POR EL MOMENTO NO LO ESTOY USANDO, MODIFICARLO DEPOIS. AHORA SOLO LOGIN. test sacado del tutorial de chelin
	#se llama en cada conexion
	def handle(self):
		self.oracion=self.request.recv(1024).strip() #tamanio de ventana
		self.num=len(self.oracion)
		print "El servidor recibio la oracion: ", self.oracion, "Su numero de caracteres es: ",self.num
		self.request.send(str(self.num))

class loginHandler(SocketServer.BaseRequestHandler):
	#se llama en cada conexion. SI O SI DEBE LLAMARSE HANDLE PORQ ES UN CASO DE USO.
	def handle(self):
		##################-----..----METODOS-------------##########################################
		##################--------------------------------#########################################
		def loginprocess():
			exitoLogin=False
			while exitoLogin == False:
				self.nombreUsuario=self.request.recv(1024).strip()
				self.passwordUsuario=self.request.recv(1024).strip()
				print "Datos recibidos"
				time.sleep(1)
				with open("usernames.txt") as loginFile:
					for linea in loginFile: #
						user,passw=linea.split(",")
						passw= passw.rstrip('\n') #Esto saca el salto de linea al final de la contrasenia
						if (user == self.nombreUsuario and passw ==  self.passwordUsuario): 
							exitoLogin=True
							self.request.send("Success")
							break
				
				if (exitoLogin == False):
					print "La conexion fallo. Esperando nuevas credenciales..."
					self.request.send("failed")

			print "Usuario logeado: ",self.nombreUsuario
			print "Login exitoso!" #EN REALIDAD NO SE CIERRA PORQUE PUSIMOS SERVE FOREVER!! cambiar eso!!!


		def crearArrayMultiDimensional():
			# Creamos una list comprehension en python, es decir una lista dentro de otra lista.
			ancho, alto = 11, 7;
			Matriz = [[0 for x in range(ancho)] for y in range(alto)]
			return Matriz
		#Creamos y printeamos el tablero (esta todo en la misma funcion)
		def imprimirTablero(tablero):
			linea=0
			while linea != 7:
				print tablero[linea]
				linea+=1

		##############################################################################################

		establish=self.request.recv(1000).strip()
		print establish
		loginprocess()
		print "Creando Tablero de juego..."
		print " "
		time.sleep(1)
		tableroJuego=crearArrayMultiDimensional()
		print "Imprimiendo tablero..."
		imprimirTablero(tableroJuego)
		print " "
		print "Tablero Creado! Enviando tablero al usuario..."
		print "------END OF ACTION----"
		#data=pickle.dumps(tableroJuego) 
		#self.request.send(data)




def main():			## ruta: C:\Users\Usuario\Desktop\clientServerLoginTest
	print "Iniciando servidor..."
	host,port="localhost", 9999 #definimos el socket
	time.sleep(1)
	

	server1 = SocketServer.TCPServer((host,port),loginHandler) #le paso una tupla con EL SOCKET y el handler que voy a usar 
	print "Servidor Iniciado: Esperando conexion del cliente..."
	server1.serve_forever() #andar hasta el cierre del programa --> socket1.server_forever() // server1.handle_request() --> Cerrar despues del login




main()