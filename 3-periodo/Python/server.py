import socket
import threading

IP = "0.0.0.0"
PORT = 4040

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(socket.SOMAXCONN)


def client(c_skt, add):
    response = ''
    while response != '\x18':
        response = c_skt.recv(1024)
        print("{}: {}".format(add, response.decode("utf-8")))

        response = response.decode("utf-8")[::-1]
        c_skt.send(response.encode('utf-8'))

    print("{} has desconected...".format(add))
    c_skt.close()


print("/* Chat inciado na porta 4040 - para sair -> CTRL + X */")

while True:
    client_skt, addr = server.accept()

    print("* New Client {} \n  ".format(addr[0]))

    client_skt = threading.Thread(target=client, args=(client_skt, addr[0]))
    client_skt.start()
