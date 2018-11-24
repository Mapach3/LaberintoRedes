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

def cuadrante(tablero, pos_x, pos_y):
    tamanio_y = len(tablero[0]) - 1
    tamanio_x = len(tablero) - 1
    print tamanio_x
    print tamanio_y
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
    if (y2 > tamanio_y):
        y2 = tamanio_y
    tamanio_cuad_x = x2 - x1 + 1;
    tamanio_cuad_y = y2 - y1 + 1;

    cuadrante = [["|" for x in range(0,tamanio_cuad_x)] for y in range(0,tamanio_cuad_y)]
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
                return x,y
    print "No se pudo determinar la posicion."

matriz = crearArrayMultiDimensional()
imprimirTablero(matriz)
pos_x, pos_y = posicion_actual(matriz)
imprimirTablero(cuadrante(matriz,4,4))
raw_input("enter para salir")
