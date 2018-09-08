import socket

HOST = "192.168.0.198"
PORT = 4040

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    while True:
        response = input()
        client.send(bytes(response, 'utf8'))
        if response == '\x18':
            break

    client.close()
except ConnectionRefusedError:
    print('Error to connect on server, try again...')
