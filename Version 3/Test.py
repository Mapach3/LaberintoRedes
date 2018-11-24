ancho, alto = 15,7

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

def cuadrante(tablero, pos_x, pos_y): # 0 , 1
    x1 = pos_x - 2
    if (x1 < 0):
        x1 = 0
    #x1 = 0
    x2 = pos_x + 2
    if (x2 > 5):
        x2 = 5
    #x2 =
    y1 = pos_y - 2
    if (y1 < 0):
        y1 = 0
    y2 = pos_y + 2
    if (y2 > 17):
        y2 = 17
    tamanio_cuad_x = x2 - x1 + 1
    tamanio_cuad_y = y2 - y1 + 1
    cuadrante = [["|" for y in range(tamanio_cuad_y)] for x in range(tamanio_cuad_x)]
    cuad_x = 0
    for x in range(x1,x2+1):
        cuad_y = 0
        for y in range(y1,y2+1):
            cuadrante[cuad_x][cuad_y] = tablero[x][y]
            cuad_y += 1
        cuad_x += 1
    return cuadrante

def imprimirTablero(tablero):
	for linea in tablero:
            print linea


def posicion_actual(tablero):
    print "Determinando posicion del jugador..."
    for x,linea in enumerate(tablero):
        for y,casilla in enumerate(linea):
            if (casilla == "*"):
                print "Posicion determinada: " + str(x) + "," + str(y)
                return y,x
    print "No se pudo determinar la posicion."

def tamanio_tablero(tablero):
    return len(tablero), len(tablero[0])

def ejecutar_movimiento(direccion, pos_x, pos_y, tablero):
    #VARIABLES A DEVOLVER POR DEFECTO
    continua_juego = True
    tipo_respuesta = ""
    descripcion_respuesta = ""
    codigo_respuesta = 100
    #LOGICA
    tamanio_x, tamanio_y = tamanio_tablero(tablero)

    origen_x, origen_y = pos_x, pos_y
    print origen_x,origen_y
    destino_x, destino_y = origen_x, origen_y
    #DETERMINAR DESTINO
    if(direccion == "DER"):
        destino_x = origen_x + 1

    if(direccion == "IZQ"):
        destino_x = origen_x - 1

    if(direccion == "ARR"):
        destino_y = origen_y + 1

    if(direccion == "ABA"):
        destino_y = origen_y - 1

    #SI EXCEDE DEL TABLERO DEVUELVE WALL
    if (destino_x < 0 or destino_x > tamanio_x or destino_y < 0 or destino_y > tamanio_y):
        tipo_respuesta = "WALL"
    #SINO PREGUNTO QUE ES EL DESTINO Y DETERMINO LA RESPUESTA
    else:
        destino = tablero[destino_y][destino_x]
        print destino
        if(destino == "P"):
            tipo_respuesta = "WALL"
        if(destino == "C"):
            tipo_respuesta = "MOV"
        if(destino == "O"):
            tipo_respuesta = "GOLD"
        if(destino == "G"):
            if(self.oro_jugador > self.oro_guardia):
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
    imprimirTablero(tablero)
    return continua_juego, tipo_respuesta, codigo_respuesta

matriz = crearArrayMultiDimensional()
imprimirTablero(matriz)
pos_x, pos_y = posicion_actual(matriz)
imprimirTablero(cuadrante(matriz,pos_x,pos_y))
print ejecutar_movimiento("DER",pos_x,pos_y,matriz)

raw_input("enter para salir")
