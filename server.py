import socket


#Definir host e porta
host = input('Informe o host: ')
port = int(input('Informe a porta: '))


#Iniciar o servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)
print('Servidor aguardando conexão...')


#Sei lá o que colocar aqui
serve2, addr2 = sock.accept()
print('Conectado ao cliente {}'.format(addr2))


#Loop de repetição
while True:
    data = serve2.recv(1024)
    if not data:
        print('Cliente desconectado')
        break
    print('Cliente: ', data.decode())
    response = input('Digite algo: ')
    serve2.send(response.encode())

#Fechar a conexão
serve2.close()