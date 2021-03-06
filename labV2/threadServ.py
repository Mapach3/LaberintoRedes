import SocketServer
import time
import threading
import pickle


class miTcpHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		##################-----..----METODOS-------------##########################################
		##################--------------------------------#########################################
		def loginprocess():
			exitoLogin=False
			codigoResponse=0
			while exitoLogin == False:
				self.comando_recibido = self.request.recv(1024).strip()
				self.comando_split = self.comando_recibido.split("|")
				self.tipo_comando = self.comando_split[0]
				user_split = self.comando_split[1].split(":")
				self.nombreUsuario=user_split[1]
				password_split = self.comando_split[2].split(":")
				self.passwordUsuario=password_split[1]

				#self.loginData=self.request.recv(1024)
				#print "LOG|user: "+self.nombreUsuario+"|pass: "+self.passwordUsuario
				#print self.loginData
				time.sleep(1)
				with open("usernames.txt") as loginFile:
					for linea in loginFile: #
						user,passw=linea.split(",")
						passw= passw.rstrip('\n') #Esto saca el salto de linea al final de la contrasenia
						if (user == self.nombreUsuario and passw ==  self.passwordUsuario): 
							exitoLogin=True
							estadoResponse = "OK"
							codigoResponse = 200
							self.request.send("LOG|" + str(codigoResponse) + "|" + estadoResponse)
							break
				
				if (exitoLogin == False):
					codigoResponse=100
					print "LOG|user: ",self.nombreUsuario+"|pass: "+self.passwordUsuario+"|"+str(codigoResponse)
					self.request.send("failed")

			#print "Usuario logeado: ",self.nombreUsuario
			print "LOG|user: ",self.nombreUsuario+"|pass: "+self.passwordUsuario+"|"+str(codigoResponse)
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

		def moverJugador(direccion, tablero):
			x,y = posicionJugador(tablero)
			x2,y2 = x,y
			if direccion=="izq":
				x2 = x-1
			if(direccion=="der"):
				x2 = x+1
			if(direccion=="abajo"):
				y2 = y-1
			if(direccion=="arriba"):
				y2 = y+1
			origen = tablero[x][y]
			destino = tablero[x2][y2]
			se_movio = True
			if (destino == "K"):
				respuesta = "KEY|descripcion:Has agarrado la llave."
			if (destino == "G"):
				if(self.oro_jugador >= self.oro_guardia):
					respuesta = "PAY|descripcion:Has pagado y te han dejado pasar."
				else:
					respuesta = "LOST|descripcion:No tienes el oro necesario para pasar, te han matado :("

				
			if (destino == "P"):
				se_movio = False
				respuesta = "WALL|descripcion:Hay una pared."
			if (destino == "O"):
				self.oro_jugador += 100;
				respuesta = "ORO|descripcion:Has agarrado una moneda."
			if (destino == "S"):
				respuesta = "WIN|descripcion:HAS GANADO!!!!!!!!!."

			if (se_movio):
				destino = "*"
				origen = "C"
			self.request.send(respuesta)



		def posicionJugador(tablero):
			for x in range(0,7):
				for y in range(0,15):
					if (tablero[x][y] == "*"):
						return x,y
			return 0,0

		def determinarPosicion(tablero):
			position="Nada"
			for x in range(0,7):
				for y in range(0,15):
					if (tablero[x][y] == "*"):
						position = "Posicion en el tablero: [",x+1,"]","[",y+1,"]"
			return position

########################################################################################### metodos para enviar cuadrante al usuario
                #Basicamente consiste en crear otra list comprehension (listForSending) de 5x5, que a medida que reccoramos la matriz original vaya poniendo los datos
		# correctos (es decir los que estan alrededor de * que es la posicion actual del jugador) y devuelva listForSending con los datos correctos

		def imprimirMatrizParaUsuario(tablero):
			linea=0
			while linea!= 4:
				print tablero[linea]
				linea+=1

		def determinarCuadrante(tablero):
			posx,posy=0,0
			for x in range(0,7):
				for y in range(0,15):
					if (tablero[x][y] == "*"):
						posx,posy=x,y

                # ESTOS IF SIRVEN PARA LIMITAR LO QUE SE RECORRE Y SE PONE EN listForSending, segun lo que dice el enunciado
		#Limitar la posicion EN Y para evitar que se vaya out of range #works
		#SE IMPRIME DOS PARA ATRAS Y DOS PARA ADELANTE SEGUN ENUNCIADO
			if posy==12 or posy==13 or posy==14:
				endY=15
			else: endY=posy+3
			if posy==0 or posy==1:
				startY=0
			else: startY=posy-2

			#Limitar la posicion en X #works
			#SE IMPRIME UNO PARA ARRIBA Y 2 PARA ABAJO SEGUN ENUNCIADO
			if posx==0 or posx==1:
				startX=0
			else: startX=posx-1
			if posx==6 or posx==7:
				endX=7
			else: endX=posx+3	
			
			#Recorrer la matriz en base a lo definido para imprimir solo el cuadrante que se pide
			listForSending= [["|" for x in range(0,5)] for y in range(0,5)]			#hacerlo de 5 porque sino supera el index y anda mal!!!!
			forUserX=0
			forUserY=0
			for x in range(startX,endX):
				forUserY=0
				for y in range(startY,endY):
					#print (Matriz[x][y]," ",end='')
					listForSending[forUserX][forUserY]=tablero[x][y] 		#esta bugeado as fuck para algunos valores, averiguar por que
					forUserY+=1
				forUserX+=1

				#print('\n')

			imprimirMatrizParaUsuario(listForSending)

			return listForSending
			

		########################################################################################################### fin metodos para enviar cuadrante al usuario


		##############################################################################################
		establish=self.request.recv(1024).strip() #definir todos los tamanios de ventana en 1024
		print establish
		loginprocess()
		print "Creando Tablero de juego..."
		print " "
		time.sleep(1)
		self.tableroJuego=crearArrayMultiDimensional()
		self.oro_jugador = 0
		self.oro_guardia = 100
		print "Imprimiendo tablero Completo (TEST) ..."
		imprimirTablero(self.tableroJuego)				#esto imprime el tablero en la consola del server
		print "Cuadrante a enviar (TEST): "
		tabSoloCuadrante=determinarCuadrante(self.tableroJuego)
		print " "
		print "Tablero Creado! Enviando tablero al usuario..."
		#tab_serializado=pickle.dumps(tableroJuego)
		tabCuadrante_serial=pickle.dumps(tabSoloCuadrante)
		#self.request.send(tab_serializado)
		self.request.send(tabCuadrante_serial)
		print determinarPosicion(self.tableroJuego)
		position = determinarPosicion(self.tableroJuego)
		self.request.send(str(position))
		tipo_respuesta = ""
		self.comando_recibido = self.request.recv(1024)
		self.comando_split = self.comando_recibido.split("|")
		self.tipo_comando = self.comando_split[0]
		if(self.tipo_comando == "MOV"):
			self.direccion_split = self.comando_split[1].split(":")
			self.direccion = self.direccion_split[1]
			moverJugador(self.direccion, self.tableroJuego)
			print "Imprimiendo tablero Completo (TEST) ..."
			imprimirTablero(self.tableroJuego)				#esto imprime el tablero en la consola del server
			print "Cuadrante a enviar (TEST): "
			tabSoloCuadrante=determinarCuadrante(self.tableroJuego)
			print " "
			print "Tablero Creado! Enviando tablero al usuario..."
			#tab_serializado=pickle.dumps(tableroJuego)
			tabCuadrante_serial=pickle.dumps(tabSoloCuadrante)
			#self.request.send(tab_serializado)
			self.request.send(tabCuadrante_serial)

		print "------END OF ACTION----"



class ThreadServer(SocketServer.ThreadingMixIn,SocketServer.ForkingTCPServer):
	pass


def main():
	print "INICIANDO SERVIDOR"
	host="localhost"
	port=9999
	time.sleep(1)
	code=200
	if (host,port) == ("localhost",9999):
		code=100
		server=ThreadServer((host,port),miTcpHandler)
		server_thread=threading.Thread(target=server.serve_forever)
		server_thread.start()
		print "SERVIDOR CORRIENDO"
	else:
		code=200
		print "RUNNING|",code


main()