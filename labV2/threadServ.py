import SocketServer
import time
import threading



class miTcpHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		data=""
		while data != "salir":
			try:
				data=self.request.recv(1024)
				if (data=="log"):
					print "log prueba"
				elif (data=="move"):
					print "move prueba"
				elif (data=="salir"): 
					print "cerrar server"
					break
				time.sleep(0.1)
			except: 
				print "El cliente D/C o hubo un error"
				data="salir"



class ThreadServer(SocketServer.ThreadingMixIn,SocketServer.ForkingTCPServer):
	pass


def main():
	host="localhost"
	port=9999
	server=ThreadServer((host,port),miTcpHandler)
	server_thread=threading.Thread(target=server.serve_forever)
	server_thread.start()
	print "SERVER RUNNING"


main()