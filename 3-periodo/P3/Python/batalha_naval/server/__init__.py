from xmlrpc.server import SimpleXMLRPCServer
from copy import deepcopy
from typing import Tuple


maps = []
players = []
TAM = 14

# 12 X 12 com bordas


def init_maps() -> list:
    player1 = [[-1 for _ in range(TAM)]]

    for _ in range(1, 13):
        line = [-1]
        line += [0 for _ in range(TAM - 2)]
        line.append(-1)
        player1.append(line)

    player1.append([-1 for _ in range(TAM)])
    player2 = deepcopy(player1)
    return [player1, player2]


def print_map(matrix):
    for k in range(1, TAM - 1):
        print(matrix[k])


def set_poss(player, siz, poss, orientation) -> bool:
    print('Player: ', player)
    print('Tamanho da embarcação: ', siz)
    print('Posição: ', poss)
    print('Orientação ', orientation)

    length = (poss[0] -1, poss[0] + siz)
    width = (poss[1] -1, poss[1] + 3)

    if orientation == 'V':
        length, width = width, length

    print_map(maps[player])
    print('Blocos: ')
    for i in range(width[0], width[1]):
        for j in range(length[0], length[1]):
            print(maps[player][i][j])
            if maps[player][i][j] != 0 and maps[player][i][j] != -1:
                return False

    for i in range(siz):
        print('I: ', i)
        if orientation == 'V':
            maps[player][poss[0] + i][poss[1]] = siz
        else:
            maps[player][poss[0]][poss[1] + i] = siz
    print_map(maps[player])

    return True


def start(player):
    players[player] = True


def login() -> int:
    global players
    if len(players) < 2:
        players.append(False)
        return len(players) - 1

    return -1


def main():
    print('Server init...')
    server = SimpleXMLRPCServer(('0.0.0.0', 9999))

    server.register_function(login)
    server.register_function(set_poss)

    print('Ctrl + C to end')
    server.serve_forever()


if __name__ == '__main__':
    maps = init_maps()
    main()
