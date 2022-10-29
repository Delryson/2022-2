from datetime import datetime #lib pra mostrar data e hora

import Pyro4

@Pyro4.expose
class Chat(object):
    def send_message(self, text):
        now = datetime.now()
        print(f'{text} - received at {now:%H:%M:%S} \n') #mostra a msg e o horario

def start_server():
    daemon = Pyro4.Daemon()             #aqui funciona a parte "RMI" do servidor:
    ns = Pyro4.locateNS()               #todas as chamadas de metodos sao executadas pelo pyro4
    uri = daemon.register(Chat)         #nesta linha, o name server procura os enderecos e faz a conexao 
    ns.register('regente.server', str(uri))
    print(f'Ready to listen')
    daemon.requestLoop()


if __name__ == '__main__':
    try:
        start_server()
    except (KeyboardInterrupt, EOFError): #pressione Ctrl+C para terminar a execucao (cmd windows)
        print('Conexao encerrada')
exit