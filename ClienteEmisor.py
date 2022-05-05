import socket
import serial

#En host se coloca la IP pública del Servidor y el port es el mismo
host = '201.170.0.74'
port = 5005
#Parametros para la configuracion de arduino
portArduino = 'COM3'
baudios = 9600

#Se crea el objeto socket para la conexión con el Servidor
objsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
objsocket.connect((host,port))
print("Inicia cliente")
objsocket.send("Emisor".encode('utf-8'))
#Se crea el objeto arduino asginandole el puerto COM y la velocidad en baudios
try:
	arduino = serial.Serial(portArduino, baudios)
except:
	print('Cannot conect to the port')

#El siguiente ciclo While repite la lectura de arduino y lo envia 
#al servidor, ademas recibe el mensaje del servidor 
while True:
	#time.sleep(0)
	lectura = arduino.readline()	#Realiza la lectura de arduino
	enviar = lectura				#La lectura se guarda en la variable enviar
	objsocket.send(enviar)			#Se envia el mensaje al Servidor
arduino.close()		#Finaliza la conexion a arduino
objsocket.close()	#Finaliza la conexion con el Servidor