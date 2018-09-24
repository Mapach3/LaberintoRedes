#usuarioIngresado="guido"
#passwordIngresada="guido333"
#loginSuccess=False

def randomTestForLogin():
	userIngr="juan"
	passIngr="juan444"
	loginSuccess=False
	with open("usernames.txt") as loginFile:
		for line in loginFile:
			print "Linea leida: ",line
			user,passw=line.split(",")
			user
			print "Usuario: ",user
			print "Password: ",passw
			if (userIngr == user and passIngr == passw):
				loginSuccess=True
				break

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


#crearArrayMultiDimensional() 


archivo=open("usernames.txt","r")
cnt=0
while cnt <=3:
	linea=archivo.readline(36)
	user,contra=linea.split(",")
	contra=contra.rstrip('\n')
	print "Dato extraido: "
	print user
	print contra
	print "Fin dato extraido"
	comparUser="guido"
	comparContr="guido333"
	if (contra == comparContr):
		print "SUCCESSFUL"
		break
	cnt+=1
	print linea
