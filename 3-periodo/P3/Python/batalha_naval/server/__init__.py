from xmlrpc.server import SimpleXMLRPCServer
from copy import deepcopy


def main():
    print('Server init...')
    server = SimpleXMLRPCServer(('0.0.0.0', 9999))
    print('Ctrl + C to end')
    server.serve_forever()


map_server = []
map_client = []
TAM = 14


# 12 X 12 com bordas
def init():
    global map_client, map_server

    map_server.append([-1 for _ in range(TAM)])

    for i in range(1, 13):
        line = [-1]
        line += [0 for _ in range(TAM - 2)]
        line.append(-1)
        map_server.append(line)

    map_server.append([-1 for _ in range(TAM)])
    map_c = deepcopy(map_server)
    return map_server, map_c


def print_block(block):
    if block == 1:
        print('\033[7;31m[X]\033[7;30m \033[m', end='')
    elif block == 6:
        print('\033[7;32m[V]\033[7;30m \033[m', end='')
    else:
        print('\033[7;30m[ ] \033[m', end='')


def print_line(matrix, i):
    for j in range(1, TAM - 1):
        print_block(matrix[i][j])


def print_maps():
    print('Mapa do Cliente', ' ' * 46, 'Mapa do Servidor', '\n   ', end='')
    for k in range(1, TAM - 1):
        print(str(k), end='   ' if k < 9 else '  ')

    print(' ' * 16, end='')
    for k in range(1, TAM - 1):
        print(str(k), end='   ' if k < 9 else '  ')

    print()
    for i in range(1, TAM - 1):
        print(chr(ord('B') + i - 1), end=' ')
        print_line(map_client, i)
        print(' ' * 12, chr(ord('B') + i - 1), end=' ')
        print_line(map_client, i)
        print()


def print_map(matrix):
    print('Mapa \n', end='   ')
    for k in range(1, TAM - 1):
        print(str(k), end='   ' if k < 9 else '  ')

    print()
    for i in range(1, TAM - 1):
        print(chr(ord('B') + i - 1), end=' ')
        print_line(matrix, i)
        print()


def is_valid(matrix, coo, tam, orientation):
    A = 65
    if len(coo) == 3:
        if coo[0].isalpha() and coo[2].isdigit():
            coord = coo.split(' ')
            coord[0], coord[1] = ord(coord[0]) - A, int(coord[1])

            if 0 < coord[1] < 13 and 0 < coord[0] < 13:
                if orientation.upper() == 'V':
                    pass
                else:
                    pass
                    # if matrix[coord[0]][coord[1]] == 0:
                    #    return True

    return False


'''
    5 = 1x Porta-aviões
    4 = 2x Encouraçados 
    3 = 3x Cruzadores 
    2 = 4x subimarinos
'''


def fill_map():
    ori = input('vertical ou horizontal [v/H]?')
    coo = input('Digite a coordenada que sera o começo da embarcação. Ex: B 1: ')


if __name__ == '__main__':
    map_server, map_client = init()
    print('Batalha naval')
    print('Primeiro preencha seu mapa de defesa')
    print_map(map_client)

    print(ord('B'))
