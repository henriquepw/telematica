import socket

IP = '0.0.0.0'
PORT = 1159

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(socket.SOMAXCONN)

print("/* Telefone sem fio na porta 1159 - para sair -> CTRL + X */")
while True:
    client_skt, addr = server.accept()
    response = client_skt.recv(1024)

    print("{}: {}".format(addr[0], response.decode("utf-8")))
    client_skt.close()
    add = input('Proximo: ')

    client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_skt.connect((add, int(PORT)))
        client_skt.send(response)
    except socket.error as e:
        print(e)

    client_skt.close()
