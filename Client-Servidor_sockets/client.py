import socket

HOST = '127.0.0.1'
PORT = 54321

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.connect((HOST, PORT))
sckt.sendall(str.encode('Relôu uôurdi!'))

data = sckt.recv(1024)

print ('Mensagem enviada: ', data.decode())

