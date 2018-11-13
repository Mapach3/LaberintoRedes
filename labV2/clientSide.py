import socket
import pickle #esto es para mandar el laberinto
import time


def main():
	host="localhost"
	port=9999
	socket1=socket.socket()
	socket1.connect((host,port))
	action="connect"


	while action!="salir":
		action=raw_input("COM: ")
		socket1.send(action)

	socket1.close()

main()





