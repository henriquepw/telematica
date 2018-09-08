import socket
import threading


def client(c_skt, add):
    response = ''
    while response != '\x18':
        response = c_skt.recv(1024).decode("utf-8")
        print("{}: {}".format(add, response))

    print("{} has desconected...".format(add))
    c_skt.close()


IP = "0.0.0.0"
PORT = 4040

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(socket.SOMAXCONN)

print("/* Chat int - para sair -> CTRL + X */")

while True:
    client_skt, addr = server.accept()

    print("* New Client {} \n  ".format(addr[0]))

    client_skt = threading.Thread(target=client, args=(client_skt, addr[0]))
    client_skt.start()
