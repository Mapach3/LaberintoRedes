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
			print "Login exitoso!" 


		def crearArrayMultiDimensional():
			# Creamos una list comprehension en python, es decir una lista dentro de otra lista.
			ancho, alto = 15, 7;
			Matriz = [["P" for x in range(ancho)] for y in range(alto)]
			# armado de tablero, segun el enunciado que nos dio damian.
			for x in range(0,ancho):
				Matriz[0][x]="P"
				Matriz[6][x]="P"
			for x in range(0,alto):
				if (x==1):
					Matriz[x][0]="*" #posicion inicial/actual va con * en vez de E de entrada
				else:
					Matriz[x][0]="P"
				Matriz[x][14]="P"
			for x in range(1,alto):
				Matriz[x][4]="C"
				Matriz[x][8]="C"
			
			Matriz[1][1]="C"	# esto se podria automatizar con un for pero no tengo ganas ahora de hacerlo..
			Matriz[1][2]="C"
			Matriz[1][3]="C"
			Matriz[1][8]="C"
			Matriz[1][9]="C"
			Matriz[1][10]="C"
			Matriz[1][11]="C"
			Matriz[1][12]="C"
			Matriz[1][13]="C" #cambiar a c
			
			Matriz[3][5]="C"
			Matriz[3][6]="C"
			Matriz[3][7]="C"

			Matriz[4][4]="C"
			Matriz[4][8]="C"
			Matriz[4][9]="C"
			Matriz[4][10]="C"
			Matriz[4][11]="C"
			Matriz[4][12]="C"
			Matriz[4][13]="C" #este campo esta en duda porque esta marcado pero no forma parte del camino por asi decirlo

			Matriz[5][6]="C"
			Matriz[5][7]="C"
			Matriz[5][11]="C"

			Matriz[6][3]="C"	
			Matriz[6][9]="C"
			Matriz[6][10]="C"
			Matriz[6][11]="C"
			
			return Matriz
		#printeamos el tablero
		def imprimirTablero(tablero):
			linea=0
			while linea != 7:
				print tablero[linea]
				linea+=1
		def determinarPosicion(tablero):
			for x in range(0,7):
				for y in range(0,15):
					if (tablero[x][y] == "*"):
						position = "Posicion del tablero: [",x+1,"]","[",y+1,"]"
			return position


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
		tab_serializado=pickle.dumps(tableroJuego)
		self.request.send(tab_serializado)
		print determinarPosicion(tableroJuego)
		position = determinarPosicion(tableroJuego)
		self.request.send(str(position))

		print "------END OF ACTION----"




def main():			## ruta: C:\Users\Usuario\Desktop\clientServerLoginTest
	print "Iniciando servidor..."
	host,port="localhost", 9999 #definimos el socket
	time.sleep(1)
	

	server1 = SocketServer.TCPServer((host,port),loginHandler) #le paso una tupla con EL SOCKET y el handler que voy a usar 
	print "Servidor Iniciado: Esperando conexion del cliente..."
	server1.serve_forever() #andar hasta el cierre del programa --> socket1.server_forever() // server1.handle_request() --> Cerrar despues del login




main()