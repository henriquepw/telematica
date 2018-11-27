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
        print('\033[7;31m[-]\033[m ', end='')
    elif block == 6:
        print('\033[7;92m[X]\033[m ', end='')
    else:
        if visible and block in (2, 3, 4, 5):
            print('\033[7;94m[{}]\033[m '.format(block), end='')
        else:
            print('\033[7;94m[ ]\033[m ', end='')


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
        print_line(map_def, i, True)
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


def get_position(msg='Digite a posição inicial da embarcação, EX: B1: ', orientation='d', siz=1) -> list:
    A = 65
    coo = ['A', 0]
    while True:
        poss = input(msg).upper()
        
        if poss[0].isalpha() and poss[1:].isdigit():
            coo[0], coo[1] = ord(poss[0]) - A, int(poss[1:])

            if orientation == 'd':
                if 0 < coo[1] < 13 and 0 < coo[0] < 13:
                    break
            elif orientation == 'H':
                if 0 < coo[1] < (14 - siz) and 0 < coo[0] < 13:
                    break
            elif orientation == 'V':
                if 0 < coo[1] < 13 and 0 < coo[0] < (14 - siz):
                    break

            print('Possição invalida, tente novamente')
        else:
            print('Possição invalida, tente novamente')

    return coo


def game(msg: str, login: int):
    global server, map_atk, map_def
    if(msg == 'Aguardando o outro jogador...'):
        print(msg)
        while True:
            if server.waiting():
                break
            time.sleep(2)

    # Pronto pra jogar -----
    print('Todos prontos')
    while True:
        if server.get_winner() != -1 or server.get_players() == 0:
            break

        if (server.get_turn() == login):
            map_atk, map_def = server.get_maps(login)
            print_maps()

            poss = get_position(
                msg='Sua vez, escolhar um bloco para atacar, EX: B1: ')
            result, map_atk, map_def = server.played(login, poss)

            print('Bem no alvo!' if result else 'Errou')  

            if server.check_winner(login):
                break

            server.set_turn(server.next(login))
            print_maps()
            print('Aguardando')
        else:  # esperando
            time.sleep(2)

    print('Fim do jogo')
    if server.get_winner() == login:
        print('Vitoria')
    else:
        print('Derrota')

    server.reset()


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
                siz = enbacations[e][0]
                orientation = get_orientation()
                poss = get_position(orientation=orientation, siz=siz)

                if server.set_poss(login, siz, poss, orientation):
                    for i in range(siz):
                        if orientation == 'V':
                            map_def[poss[0] + i][poss[1]] = siz
                        else:
                            map_def[poss[0]][poss[1] + i] = siz
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
     6 = Tiro Certo
'''

if __name__ == '__main__':
    ip = input('Digite o ip do servidor: ')
    server = xmlrpc.client.ServerProxy('http://'+ ip +':9999')
    map_def, map_atk = init_maps()
    init()
