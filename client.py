#Importações
import socket


#Definir host e porta
host = input('Digite o host: ')
port = int(input('Digite a porta: '))


#Configurações do client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))


#Loop infinito
while True:
    data = input('Digite algo: ')
    sock.send(data.encode())
    response = sock.recv(1024)
    print(response.decode())

#Fechar a conexão
sock.close()