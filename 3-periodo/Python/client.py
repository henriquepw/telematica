import socket

HOST = "192.168.0.198"
PORT = 4040

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    response = input()
    if response == '\x18':
        break
    client.send(bytes(response, 'utf8'))

client.close()
