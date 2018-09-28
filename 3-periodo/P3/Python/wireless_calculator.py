import socket


def calculator(sinal, numeros) -> float:
    result = numeros[0]
    if sinal == '+':
        result += numeros[1]
    elif sinal == '-':
        result -= numeros[1]
    elif sinal == '/':
        result /= numeros[1]
    elif sinal == '*':
        result *= numeros[1]

    return result


operators = ['+', '-', '/', '*']
IP = '0.0.0.0'
PORT = 1159

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(socket.SOMAXCONN)

print("/* Telefone sem fio - 1159 */")
while True:
    client_skt, addr = server.accept()
    response = client_skt.recv(1024).decode("utf-8")

    out = response
    if response[0] in operators:
        sign, numbers, num = response[0], response[1:].split(','), []
        try:
            num = [float(x) for x in numbers]
            out = calculator(sign, num)
        except ValueError:
            print('Erro na operacao')

    print(out)

    client_skt.close()
    add = input('Proximo: ')

    client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_skt.connect((add, int(PORT)))
        client_skt.send(bytes(response, 'utf8'))
    except socket.error as e:
        print(e)

    client_skt.close()
