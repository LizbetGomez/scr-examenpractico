import socket
import threading

#Parametros para el server
host = ''
port = 5005

#Se crea el objeto server para iniciar el Servidor, Con la configuración de la ip y el puerto asignado
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

#Se indica al server que escuche para recibir la conexión
server.listen(2)
print ("Servidor en espera...")

#Declaracion de arreglos
clients = []
functions = []

#funcion para recibir mensajes del cliente, emisor
def recibir(client, etiqueta):
	if etiqueta == "Emisor":
		while True:
			recibido = client.recv(1024)
			print(recibido)
	return recibido

#funcion para enviar mensajes al receptor
def enviar(client, etiqueta, recibido):
	if etiqueta == "Receptor":
		while True:
			enviar = recibido		#Se guarda el mensaje de recibido
			client.send(enviar.encode(encoding="ascii", errors="ignore"))#Se envia el valor al receptor

while True:

	#Se obtiene la direccion del cliente conectado
	client, address = server.accept()
	function = client.recv(1024) #Recibe la etiqueta del cliente

	functions.append(function)
	clients.append(client) #Se agregan a los arreglos

	print("La funcion del cliente es :", function.decode(encoding="ascii", errors="ignore")) #Escribe la funcion del cliente

	etiqueta = function.decode(encoding="ascii", errors="ignore")
	recibido = "b'1'"
	#se crean los hilos para las funciones de recibir y enviar
	thread1 = threading.Thread(target=recibir, args=(client, etiqueta,))
	thread1.start()
	thread2 = threading.Thread(target=enviar, args=(client, etiqueta, recibido))
	thread2.start()
	
client.close() #Finaliza la conexion