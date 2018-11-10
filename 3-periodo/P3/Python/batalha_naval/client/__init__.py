import xmlrpc.client
from copy import deepcopy
from typing import Tuple

server = xmlrpc.client.ServerProxy('http://localhost:9999')

map_def = []
map_atk = []
TAM = 14


def print_block(block, visible):
    if block == 1:
        print('\033[7;31m[X]\033[7;30m \033[m', end='')
    elif block == 6:
        print('\033[7;32m[V]\033[7;30m \033[m', end='')
    else:
        if visible:
            print('\033[7;30m[',block,'] \033[m', end='')
        else:
            print('\033[7;30m[ ] \033[m', end='')


def print_line(matrix, i, visible):
    for j in range(1, TAM - 1):
        print_block(matrix[i][j], visible)


def print_maps(visible=False):
    print('Mapa de Ataque', ' ' * 46, 'Mapa de defesa', '\n   ', end='')
    for k in range(1, TAM - 1):
        print(str(k), end='   ' if k < 9 else '  ')

    print(' ' * 16, end='')
    for k in range(1, TAM - 1):
        print(str(k), end='   ' if k < 9 else '  ')

    print()
    for i in range(1, TAM - 1):
        print(chr(ord('B') + i - 1), end=' ')
        print_line(map_atk, i, visible)
        print(' ' * 12, chr(ord('B') + i - 1), end=' ')
        print_line(map_def, i, visible)
        print()


def print_map(matrix, visible=False):
    print('Mapa \n', end='   ')
    for k in range(1, TAM - 1):
        print(str(k), end='   ' if k < 9 else '  ')

    print()
    for i in range(1, TAM - 1):
        print(chr(ord('B') + i - 1), end=' ')
        print_line(matrix, i, visible)
        print()


def init_maps() -> Tuple[list, list]:
    global map_def, map_atk

    map_atk.append([-1 for _ in range(TAM)])
    for __ in range(1, 13):
        line = [-1]
        line += [0 for _ in range(TAM - 2)]
        line.append(-1)
        map_atk.append(line)

    map_atk.append([-1 for _ in range(TAM)])
    map_def = deepcopy(map_atk)
    return map_def, map_atk


def get_orientation() -> chr:
    while True:
        orientation = input('Horientação da embarcação (v/H)').upper()
        if len(orientation) == 1 and (orientation == 'V' or orientation == 'H'):
            break
        else:
            print('Horientação invalidam, tente novamente')

    return orientation


def get_position() -> list:
    A = 65
    coo = ['A', 0]
    while True:
        poss = input(
            'Digite a posição inicial da embarcação, EX: B1: ').upper()
        if len(poss) == 2 and poss[0].isalpha() and poss[1].isdigit():
            coo[0], coo[1] = ord(poss[0]) - A, int(poss[1])

            if 0 < coo[1] < 13 and 0 < coo[0] < 13:
                break
            else:
                print('Possição invalida, tente novamente')
        else:
            print('Possição invalida, tente novamente')

    return coo


def init():
    global server, map_def
    login = server.login()
    if login > -1:
        enbacations = {
            'subimarinos': [2, 4],
            'Cruzadores': [3, 3],
            'Encouraçados': [4, 2],
            'porta-aviões': [5, 1]}

        print('Batalha naval')
        print('Peenchar sua mapa de defesa')
        print_map(map_def)

        for e in enbacations.keys():
            print('Peenchar os ' + e + ' ')
            j = 0
            while enbacations[e][1] != j:
                orientation, poss = get_orientation(), get_position()

                if server.set_poss(login, enbacations[e][0], poss, orientation):
                    for i in range(enbacations[e][0]):
                        if orientation == 'V':
                            map_def[poss[0] + i][poss[1]] = enbacations[e][0]
                        else:
                            map_def[poss[0]][poss[1] + i] = enbacations[e][0]
                    print_map(map_def, visible=True)
                    j += 1
                else:
                    print('Posição invalida.')
        server.ready(login)
    else:
        print('Sem vagas')


'''
    Significado dos numeros nas matrizes
    -1 = Lugar invalido
     1 = tiro Errado
     2 = 4x subimarinos
     3 = 3x Cruzadores
     4 = 2x Encouraçados 
     5 = 1x Porta-aviões
     6 = Tiro Certo
'''
if __name__ == '__main__':
    map_def, map_atk = init_maps()
    init()
