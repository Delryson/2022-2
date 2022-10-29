import socket  #Biblioteca para usar sockets

HOST = "localhost"
PORT = 54321

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#o parãmetro AF_INET é a família IPV4, e o SOCK_STREAM é o indica o protocolo TCP 

#fazendo o vínculo (bind) entre host e a porta
server.bind((HOST, PORT))

#colocando o server em modo de escuta
server.listen()

print ("Aguardando conexão em %s:%d" % (HOST,PORT))
#Exibindo uma mensagem para mostrar que o server está ativo

conexao, endereco = server.accept()
#setando os parametros do metodo accept pra pegar a conexao e o endereco

print ('Conexão bem sucedida em ', endereco)
#Para mostrar que a conexao foi bem sucedida

while True:
    dados = conexao.recv(1024)
    #uma variavel para receber os dados, como um buffer de tamanho 1024 bytes
    conexao.sendall(dados) #enviando todos os dados
    if not dados: #caso não tenha mais dados, a conexão é encerrada
        print ('Encerrando conexão...')
        conexao.close()
        break
    

    