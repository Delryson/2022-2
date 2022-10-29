from datetime import datetime

import Pyro4

server = Pyro4.Proxy(f"PYRONAME:regente.server") #Aqui ocorre a conexao C/S com algo parecido com um STUB

def start_chatting(): #comeca conexao via "stubs" do pyro.naming
    text = ''
    while (text != 'exit'):  #digite exit para encerrar o chat
        text = input("... ")
        now = datetime.now()
        server.send_message(text) #manda a msg para o name server, que faz a conexao procurando o servidor aberto pelo nome dele
        print(f'sent at {now:%H:%M:%S} \n')

if __name__ == '__main__':
    try:
        start_chatting()
    except (KeyboardInterrupt, EOFError): #pressione Ctrl+C para terminar a execucao (cmd windows)
        print('Esta conversa acaba aqui! -_-')
exit