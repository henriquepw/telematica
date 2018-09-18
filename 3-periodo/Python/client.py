import socket

host = '192.168.0.198'
post = '4040'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host, post = input('Host:port: ').split(':')

try:
    client.connect((host, int(post)))
    while True:
        response = input()
        client.send(bytes(response, 'utf8'))
        if response == '\x18':
            break
        print(client.recv(1024).decode('utf-8'))

    client.close()
except ConnectionRefusedError:
    print('Error to connect on server, try again...')
