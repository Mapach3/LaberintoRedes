import socket
import pickle
import time

print "Bienvenido cliente: "
host="localhost"
port=9999
socket1=socket.socket()
socket1.connect((host,port))
code=100
socket1.send("EST|"+str(host)+"|"+str(port)+"|"+str(code))
respuesta = socket1.recv(1024).split("|")
print respuesta
tipo_respuesta = respuesta[0]
codigo_respuesta = respuesta[1]
if(tipo_respuesta == "EST"):
    if(codigo_respuesta == "200"):
        print "Conexion exitosa."
    else:
        print "Conexion fallida."
else:
    print "Error > se esperaba comando EST"

def loguearse():
        print "Iniciando login..."
        logeado = False
        while (logeado == False):
            usuario = raw_input("Usuario --> ")
            contrasenia = raw_input("Contrasenia --> ")
            socket1.send("LOG|"+str(usuario)+"|"+str(contrasenia))
            respuesta = socket1.recv(1024).split("|")
            tipo_respuesta = respuesta[0]
            codigo_respuesta = respuesta[1]
            if(tipo_respuesta == "LOG"):
                if(codigo_respuesta == "200"):
                    logeado = True
                    print "Logeo exitosa."
                else:
                    print "Logeo fallido."
            else:
                print "Error > se esperaba comando LOG"

def recibir_cuadrante():
    print "Esperando cuadrante..."
    time.sleep(1)
    respuesta = socket1.recv(1024).split("|")
    tipo_respuesta = respuesta[0]
    codigo_respuesta = respuesta[1]
    if(tipo_respuesta == "SEND"):
        if(codigo_respuesta == "200"):
            print "Cuadrante recibido."
            cuadrante = respuesta[2]
            cuadrante_deserializado = pickle.loads(cuadrante)
            return cuadrante_deserializado
        else:
            print "Error al recibir el cuadrante."
    else:
        print "Error > se esperaba comando SEND"

def main():
    loguearse()
    #PASO 3 - RECIBIR CUADRANTE
    cuadrante = recibir_cuadrante()
    print cuadrante
    raw_input("toca enter para salir")
    #PASO 4 - MOVERSE


main()
