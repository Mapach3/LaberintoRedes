##SERVIDOR##
import SocketServer

class miTcpHandler(SocketServer.BaseRequestHandler):		#POR EL MOMENTO NO LO ESTOY USANDO, MODIFICARLO DEPOIS. AHORA SOLO LOGIN.
	#se llama en cada conexion
	def handle(self):
		self.oracion=self.request.recv(1024).strip() #tamanio de ventana
		self.num=len(self.oracion)
		print "El servidor recibio la oracion: ", self.oracion, "Su numero de caracteres es: ",self.num
		self.request.send(str(self.num))

class loginHandler(SocketServer.BaseRequestHandler):
	#se llama en cada conexion. SI O SI DEBE LLAMARSE HANDLE PORQ ES UN CASO DE USO.
	def handle(self):
		exitoLogin=False
		while exitoLogin == False:
			self.nombreUsuario=self.request.recv(1024).strip()
			self.passwordUsuario=self.request.recv(1024).strip()
			print "Usuario Ingresado: ",self.nombreUsuario
			print "Contrasenia Ingresada: ",self.passwordUsuario
			with open("usernames.txt") as loginFile:
				for linea in loginFile:
					user,passw=linea.split(",")
					print user
					print passw
					if (user == self.nombreUsuario and  passw == self.passwordUsuario):
						exitoLogin=True
			
			if (exitoLogin == False):
				print "La conexion fallo"
				print "Estado del login: ",exitoLogin
				self.request.send("failed")

		print "Usuario logeado: ",self.nombreUsuario
		print "El servidor se cerrara." #EN REALIDAD NO SE CIERRA PORQUE PUSIMOS SERVE FOREVER!! cambiar eso!!!
		self.request.send("Success")



	






def main():
	print "Prueba del servidor"
	host="localhost" #direccion
	port=9999

	server1 = SocketServer.TCPServer((host,port),loginHandler) #le paso una tupla con EL SOCKET y el handler
	print "El server esta corriendo"
	server1.serve_forever() #andar hasta el cierre del programa




main()
