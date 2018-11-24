import SocketServer
import time
import threading
import pickle

class miTcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.oro_jugador = 0
        self.oro_guardia = 100
        self.key_jugador = False
        def establecer_conexion():
            print "Estableciendo conexion..."
            print self.oro_guardia
            establish = self.request.recv(1024).strip() #definir todos los tamanios de ventana en 1024
            self.request.send("EST|"+str(200))
            print "Conexion establecida"

        def crear_tablero():
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

			Matriz[1][1]="O"	# esto se podria automatizar con un for pero no tengo ganas ahora de hacerlo..
			Matriz[1][2]="G"
			Matriz[1][3]="K"
			Matriz[1][8]="C"
			Matriz[1][9]="C"
			Matriz[1][10]="C"
			Matriz[1][11]="C"
			Matriz[1][12]="C"
			Matriz[1][13]="C" #cambiar a c

			Matriz[3][5]="D"
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

        def posicion_actual(tablero):
            print "Determinando posicion del jugador..."
            for x,linea in enumerate(tablero):
                for y,casilla in enumerate(linea):
                    if (casilla == "*"):
                        print "Posicion determinada: [" + str(y) + "," + str(x) + "]"
                        return y,x
            print "No se pudo determinar la posicion."

        def determinar_cuadrante(tablero, pos_x, pos_y):
            x1 = pos_x - 2
            if (x1 < 0):
                x1 = 0
            x2 = pos_x + 2
            if (x2 > 17):
                x2 = 17
            y1 = pos_y - 2
            if (y1 < 0):
                y1 = 0
            y2 = pos_y + 2
            if (y2 > 5):
                y2 = 5
            tamanio_cuad_x = x2 - x1 + 1
            tamanio_cuad_y = y2 - y1 + 1
            cuadrante = [["|" for x in range(tamanio_cuad_x)] for y in range(tamanio_cuad_y)]
            cuad_x = 0
            for x in range(x1,x2+1):
                cuad_y = 0
                for y in range(y1,y2+1):
                    cuadrante[cuad_y][cuad_x] = tablero[y][x]
                    cuad_y += 1
                cuad_x += 1
            return cuadrante

        def imprimir_matriz(matriz):
            for linea in matriz:
                print linea

        def enviar_cuadrante(cuadrante):
    		cuadrante_serializado = pickle.dumps(cuadrante)
    		self.request.send("SEND|200|" + cuadrante_serializado)

        def esperar_movimiento():
            comando_recibido = self.request.recv(1024)
            comando_split = comando_recibido.split("|")
            tipo_comando = comando_split[0]
            direccion = ""
            if(tipo_comando == "MOV"):
                direccion = comando_split[1]
            return direccion

        def ejecutar_movimiento(direccion, pos_x, pos_y, tablero):
            #VARIABLES A DEVOLVER POR DEFECTO
            continua_juego = True
            tipo_respuesta = ""
            descripcion_respuesta = ""
            codigo_respuesta = 100
            #LOGICA
            tamanio_x, tamanio_y = tamanio_tablero(tablero)
            print "tamanio y x"
            print tamanio_y, tamanio_x
            origen_x, origen_y = pos_x, pos_y
            print "origen y x"
            print origen_y,origen_x
            destino_x, destino_y = origen_x, origen_y
            #DETERMINAR DESTINO
            if(direccion == "DER"):
                destino_x = origen_x + 1

            if(direccion == "IZQ"):
                destino_x = origen_x - 1

            if(direccion == "ARR"):
                destino_y = origen_y - 1

            if(direccion == "ABA"):
                destino_y = origen_y + 1

            #SI EXCEDE DEL TABLERO DEVUELVE WALL
            if (destino_x < 0 or destino_x > tamanio_x or destino_y < 0 or destino_y > tamanio_y):
                tipo_respuesta = "WALL"
            #SINO PREGUNTO QUE ES EL DESTINO Y DETERMINO LA RESPUESTA
            else:
                destino = tablero[destino_y][destino_x]
                print "destino y x"
                print destino_y, destino_x
                print "destino"
                print destino
                if(destino == "P"):
                    tipo_respuesta = "WALL"
                if(destino == "C"):
                    tipo_respuesta = "MOV"
                if(destino == "O"):
                    self.oro_jugador += 100
                    tipo_respuesta = "GOLD"
                if(destino == "G"):
                    if(self.oro_jugador >= self.oro_guardia):
                        self.oro_jugador -= self.oro_guardia
                        tipo_respuesta = "PAY"
                    else:
                        tipo_respuesta = "LOST"

                if(destino == "K"):
                    tipo_respuesta = "KEY"
                    self.key_jugador = True
                if(destino == "D"):
                    if(self.key_jugador):
                        tipo_respuesta = "WIN"
                    else:
                        tipo_respuesta = "STOP"

                #SI NO SE MOVIO VUELVE AL ORIGEN
                se_movio = tipo_respuesta != "WALL" and tipo_respuesta != "STOP"
                if(se_movio == False):
                    destino_x, destino_y = origen_x, origen_y

                #si no gano ni perdio quiere decir que el juego continua
                continua_juego = tipo_respuesta != "WIN" and tipo_respuesta != "LOST"
            codigo_respuesta = 200
            tablero[origen_y][origen_x] = "C"
            tablero[destino_y][destino_x] = "*"
            #FIN LOGICA
            return continua_juego, tipo_respuesta, codigo_respuesta

        def enviar_respuesta_movimiento(tipo_respuesta, codigo_respuesta):
            self.request.send(tipo_respuesta + "|" + str(codigo_respuesta))

        def esperar_reinicio():
            comando_recibido = self.request.recv(1024)
            comando_split = comando_recibido.split("|")
            tipo_comando = comando_split[0]
            return tipo_comando == "RES"

        def desconectar_cliente():
            pass

        def tamanio_tablero(tablero):
            return len(tablero), len(tablero[0])

        def loguearse():
            print "Iniciando login..."
            comando_recibido = self.request.recv(1024).strip() #definir todos los tamanios de ventana en 1024
            comando_split = comando_recibido.split("|")
            tipo_comando = comando_split[0]
            usuario, contrasenia = "", ""
            if(tipo_comando == "LOG"):
                usuario = comando_split[1]
                contrasenia = comando_split[2]
                print "Datos recibidos: " + usuario + ", " + contrasenia
            if(autenticado(usuario, contrasenia)):
                respuesta = "LOG|"+str(200)
                print "Logueo exitoso"
            else:
                respuesta = "LOG|"+str(100)
                print "Logueo fallido"
            self.request.send(respuesta)

        def autenticado(usuario,contrasenia):
            time.sleep(1)
            with open("D:/Facultad Stefano/Redes/LaberintoRedes/Version 3/usernames.txt") as loginFile:
                for linea in loginFile:
                    user,passw=linea.split(",")
                    passw= passw.rstrip('\n') #Esto saca el salto de linea al final de la contrasenia
                    if (user == usuario and passw == contrasenia):
                        return True
                return False

        # PASO 1 - ESTABLECER CONEXION CON EL CLIENTE
        establecer_conexion()
        #loguearse()
        reiniciar = True
        while (reiniciar):
            time.sleep(0.1)
            # PASO 2 - CREAR TABLERO
            tablero = crear_tablero()
            # PASO 3 - JUGAR
            imprimir_matriz(tablero)
            continua_juego = True
            # PASO 3.1 - DETERMINAR POSICION DEL JUGADOR
            pos_x, pos_y = posicion_actual(tablero)

            print "Pos x y"
            print pos_x, pos_y
            # PASO 3.2 - DETERMINAR CUADRANTE
            cuadrante = determinar_cuadrante(tablero, pos_x, pos_y)
            imprimir_matriz(cuadrante)
            # PASO 3.3 - ENVIAR CUADRANTE AL JUGADOR
            enviar_cuadrante(cuadrante)
            while (continua_juego):
                time.sleep(0.1)
                # PASO 3.1 - ESPERAR MOVIMIENTO DEL JUGADOR
                direccion = esperar_movimiento()
                # PASO 3.2 - PROCESAR MOVIMIENTO DEL JUGADOR
                continua_juego, tipo_respuesta, codigo_respuesta = ejecutar_movimiento(direccion, pos_x, pos_y, tablero)
                # PASO 3.3 - ENVIAR RESPUESTA AL JUGADOR
                enviar_respuesta_movimiento(tipo_respuesta, codigo_respuesta)
                # PASO 3.4 - DETERMINAR POSICION DEL JUGADOR
                pos_x, pos_y = posicion_actual(tablero)
                # PASO 3.5 - DETERMINAR CUADRANTE
                cuadrante = determinar_cuadrante(tablero, pos_x, pos_y)
                imprimir_matriz(cuadrante)
                # PASO 3.6 - ENVIAR CUADRANTE AL JUGADOR
                enviar_cuadrante(cuadrante)
            # PASO 4 - UNA VEZ QUE GANO O PERDIO ESPERAR SI QUIERE REINICIAR
            reiniciar = esperar_reinicio()
        # PASO 5 - CERRAR CONEXION / SERVIDOR
        desconectar_cliente()




class ThreadServer(SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    pass

def main():
    print "Iniciando servidor..."
    host="localhost"
    port=9999
    code=100
    server = ThreadServer((host, port), miTcpHandler)
    server_thread = threading.Thread(target = server.serve_forever)
    server_thread.start()
    code = 200
    print "Servidor iniciado."

main()
