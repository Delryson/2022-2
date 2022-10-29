import socket

HOST = '127.0.0.1'
PORT = 54321

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.connect((HOST, PORT))
sckt.sendall(str.encode('Relôu uôurdi!')) #mensagem enviada automaticamente ao servidor

data = sckt.recv(1024) #tamanho do buffer de arquivos

print ('Mensagem enviada: ', data.decode()) #decodificando e exibindo a msg

