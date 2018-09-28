import socket
import threading as th


OPERATORS = ['+', '-', '/', '*']
IP, PORT, BUFF = '0.0.0.0', 1159, 1024
CODE = 'utf-8'


def calculator(sinal, numeros) -> str:
    result = numeros[0]
    if sinal == '+':
        result += numeros[1]
    elif sinal == '-':
        result -= numeros[1]
    elif sinal == '/':
        result /= numeros[1]
    elif sinal == '*':
        result *= numeros[1]

    return str(result)


def client(cskt, add):
    while True:
        try:
            recev = cskt.recv(BUFF).decode('utf-8')
            if recev[0] in OPERATORS:
                try:
                    nums = [float(x) for x in recev[1:].replace(' ', '').split(',')]
                    response = calculator(recev[0], nums)
                    cskt.send(response.encode(CODE))
                except ValueError:
                    cskt.send(('Numeros invalidos\n').encode(CODE))
            else:
                cskt.send(('Operador invalido\n').encode(CODE))
        except UnicodeEncodeError:
            cskt.send(('Erro na conversao para utf-8\n').encode(CODE))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(socket.SOMAXCONN)

max = socket.SOMAXCONN
print("/* Server Calculator - 1159 */")
for _ in range(max):
    client_skt, addr = server.accept()

    print("* New Client {} \n  ".format(addr[0]))

    th.Thread(target=client, args=(client_skt, addr[0])).start()
