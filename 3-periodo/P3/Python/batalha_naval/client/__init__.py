import time
import xmlrpc.client
from copy import deepcopy
from typing import Tuple

server = xmlrpc.client.ServerProxy('http://localhost:9999')

map_def = []
map_atk = []
TAM = 14


def print_block(block, visible):
    if block == 1:
        print('\033[7;31m[X]\033[m ', end='')
    elif block == 6:
        print('\033[7;32m[V]\033[m ', end='')
    else:
        if visible:
            print('\033[7;33m[', block, ']\033[m ', end='')
        else:
            print('\033[7;33m[ ]\033[m ', end='')


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


def get_position(msg='Digite a posição inicial da embarcação, EX: B1: ') -> list:
    A = 65
    coo = ['A', 0]
    while True:
        poss = input(msg).upper()
        if len(poss) == 2 and poss[0].isalpha() and poss[1].isdigit():
            coo[0], coo[1] = ord(poss[0]) - A, int(poss[1])

            if 0 < coo[1] < 13 and 0 < coo[0] < 13:
                break
            else:
                print('Possição invalida, tente novamente')
        else:
            print('Possição invalida, tente novamente')

    return coo


def game(msg: str, login: int):
    global server, map_atk, map_def
    if('Aguardando o outro jogador...'):
        print(msg)
        while True:
            if server.waiting():
                break
            time.sleep(2)
    
    map_atk = server.get_opponent(login)

    print_map(map_atk, visible=True)
    
    # Pronto pra jogar -----
    print('Todos prontos')
    while True: # serve.winner()
        if (server.get_turn() == login):
            print_maps()

            poss = get_position(msg='Sua vez, escolhar um bloco para atacar, EX: B1: ')
            result = server.played(login, poss)
            print(result)

            map_atk[poss[0]][poss[1]] = 6 if result else 1

            '''
            if result:
                map_atk[poss[0]][poss[1]] = 6
            else:
                map_atk[poss[0]][poss[1]] = 1
            '''
            print_maps()
            print('Aguardando')
        else:
            #esperondo
            time.sleep(2)


def init():
    global server, map_def
    login = server.login()
    if login > -1:
        '''
        enbacations = {
            'subimarinos': [2, 1],
            'Cruzadores': [3, 1],
            'Encouraçados': [4, 1],
            'porta-aviões': [5, 1]}
        '''

        enbacations = {
            'subimarinos': [2, 1]}

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

        game(server.ready(login), login)
    else:
        print('Sem vagas')


'''
    Significado dos numeros nas matrizes
    -1 = Lugar invalido
     0 = Água
     1 = tiro Errado
     2 = 4x subimarinos
     3 = 3x Cruzadores
     4 = 2x Encouraçados 
     5 = 1x Porta-aviões
     6 = Tiro Certo, 0
'''
if __name__ == '__main__':
    map_def, map_atk = init_maps()
    init()
