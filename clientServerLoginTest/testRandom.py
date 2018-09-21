usuarioIngresado="guido"
passwordIngresada="guido333"
loginSuccess=False


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

