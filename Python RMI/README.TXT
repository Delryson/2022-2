

O que é o PYRO?
Python Remote Object, que permite invocar um método de objeto remoto que está rodando em um outro
processo como se fosse local. Essa biblioteca é conceitualmente idêntica ao RMI do Java, e permite
distribuir e gerenciar objetos em uma conexão do tipo CLiente-Servidor.  

Por que utilizar PYRO?
Como a atividade de aplicação RPC deve utilizar, obrigatoriamente, um recurso exclusivo java (RMI)
e o programador em questão só manja de Python e C, esta lib será utilizada neste projeto em razão
do mesmo já ter uma vida atribulada demais para tentar se meter com java uma hora dessas...

Para instalar a lib via command prompt:
pip install pyro

Caso não tenha o Python instalado no computador, baixe via navegador, e instale o setup.py encontrado
em https://github.com/irmen/Pyro4.

OBS: A versão do Python utilizada é a 3.x

INSTRUÇOES PARA RODAR O PROGRAMA:
 1- Com o PYRO4 instalado, abra um terminal e digite
        python -m Pra outro terminal e execute o pyroServer.py
yro4.naming
    este comando permite instanciar um servidor configurado pelo nome

2-  Ab
3-  Abra mais outro terminal e execute o pyroClient.py

O Servidor aceita multiplas conexoes, logo pode-se instanciar quantos clientes desejar. Para instanciar
outro servidor, é necessário configurar outro servidor com outro nome.