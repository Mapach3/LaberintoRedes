import socket
import pickle
import time
print "Bienvenido cliente: "
host = "localhost"
port = 9999
socket1=socket.socket()
socket1.connect((host,port))
code=100
socket1.send("ESTABLISH |"+str(host)+"|"+str(port)+"|"+str(code))
