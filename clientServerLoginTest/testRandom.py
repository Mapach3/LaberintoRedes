#usuarioIngresado="guido"
#passwordIngresada="guido333"
#loginSuccess=False

def randomTestForLogin():
	with open("usernames.txt") as loginFile:
		for line in loginFile:
			print "Linea leida: ",line
			user,passw=line.split(",")
			print "Usuario: ",user
			print "Password: ",passw
			if (usuarioIngresado == user and passwordIngresada == passw):
				loginSuccess=True

			else: 
				pass

	if (loginSuccess):
		print "Se logeo correctamente"
	else:
		print "El usuario no fue encontrado"



#file=open("usernames.txt","r")
#linea=file.readline()
#print "Linea leida: ",linea
#user,passw=linea.split(",")
#
#print "Usuario: ",user
#print "Password: ",passw

def crearArrayMultiDimensional():

	# Creates a list containing 5 lists, each of 8 items, all set to 0
	ancho, alto = 11, 7;
	Matriz = [[0 for x in range(ancho)] for y in range(alto)]
	linea=0
	while linea != 7:
		print Matriz[linea]
		linea+=1




crearArrayMultiDimensional() 