import SocketServer
import time
import threading
import pickle

class miTcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):

        def establecer_conexion():
            print "Estableciendo conexion..."
            establish = self.request.recv(1024).strip() #definir todos los tamanios de ventana en 1024
            print establish
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

        def posicion_actual(tablero):
            print "Determinando posicion del jugador..."
            for x,linea in enumerate(tablero):
                for y,casilla in enumerate(linea):
                    if (casilla == "*"):
                        print "Posicion determinada: [" + x + "," y + "]"
                        return x,y
            print "No se pudo determinar la posicion."

        def cuadrante(tablero, pos_x, pos_y):
            tamanio_x = len(tablero[0]) - 1
            tamanio_y = len(tablero) - 1
            x1 = pos_x - 2
            if (x1 < 0):
                x1 = 0
            x2 = pos_x + 2
            if (x2 > tamanio_x):
                x2 = tamanio_x
            y1 = pos_y - 2
            if (y1 < 0):
                y1 = 0
            y2 = pos_y + 2
            if (y2 > tamanio_y)
                y2 = tamanio_y
            cuadrante = [tamanio_x][tamanio_y]
            for x in range(x1,x2):
                for y in range(y1,y2):
                    cuadrante[x][y] = tablero[x][y]
            return cuadrante



        def enviar_cuadrante(cuadrante):
            pass

        def esperar_movimiento():
            pass

        def ejecutar_movimiento():
            pass

        def enviar_respuesta_movimiento():
            pass

        def esperar_reinicio():
            pass

        def desconectar_cliente():
            pass


        # PASO 1 - ESTABLECER CONEXION CON EL CLIENTE
        establecer_conexion()

        reiniciar = True
        while (reiniciar):
            time.sleep(0.1)
            # PASO 2 - CREAR TABLERO
            tablero = crear_tablero()
            # PASO 3 - JUGAR
            while (continua_juego):
                time.sleep(0.1)
                # PASO 3.1 - DETERMINAR POSICION DEL JUGADOR
                posicion_actual = posicion_actual(tablero)
                # PASO 3.2 - DETERMINAR CUADRANTE A
                cuadrante = cuadrante(tablero, posicion_actual)
                # PASO 5.1 - ENVIAR CUADRANTE AL JUGADOR
                enviar_cuadrante(cuadrante)
                # PASO 5.2 - ESPERAR MOVIMIENTO DEL JUGADOR
                direccion = esperar_movimiento()
                # PASO 5.3 - PROCESAR MOVIMIENTO DEL JUGADOR
                continua_juego, tipo_respuesta, descripcion_respuesta = ejecutar_movimiento(direccion)
                # PASO 5.4 - ENVIAR RESPUESTA AL JUGADOR
                enviar_respuesta_movimiento(tipo_respuesta, descripcion_respuesta)
            # PASO 6 - UNA VEZ QUE GANO O PERDIO ESPERAR SI QUIERE REINICIAR
            reiniciar = esperar_reinicio()
        # PASO 7 - CERRAR CONEXION / SERVIDOR
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
