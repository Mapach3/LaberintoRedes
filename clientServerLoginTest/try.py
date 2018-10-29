from __future__ import print_function

def testMatriz():
	ancho, alto = 15,7
	Matriz = [["*" for x in range(ancho)] for y in range(alto)]
	for x in range(0,7):
		for y in range(0,15):
			Matriz[x][y]=y
	Matriz[6][14]="P"   		#POSICION
	posx,posy=determinarPosicion(Matriz)
	imprimirTablero(Matriz)
	
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
	listForSending= [["|" for x in range(0,5)] for y in range(0,5)]
	forUserX=0
	forUserY=0
	for x in range(startX,endX):
		for y in range(startY,endY):
			print (Matriz[x][y]," ",end='')
			listForSending[forUserX][forUserY]=Matriz[x][y]			#esta bugeado esto, no se porque, arreglarlo!! // update: arreglado: habia que hacer un poco mas grande el cuadrante
			forUserY+=1
		forUserX+=1
		forUserY=0

		print('\n')

	imprimirMatrizParaUsuario(listForSending)

def determinarPosicion(tablero):
	posx,posy=0,0
	for x in range(0,7):
		for y in range(0,15):
			if (tablero[x][y] == "P"):
				posx,posy=x,y
	print ("posicion: ",posx,posy)
	return posx,posy

def imprimirTablero(tablero):
			linea=0
			while linea != 7:
				print (tablero[linea])
				linea+=1

def imprimirMatrizParaUsuario(tablero):
	linea=0
	while linea!= 4:
		print(tablero[linea])
		linea+=1



testMatriz()
