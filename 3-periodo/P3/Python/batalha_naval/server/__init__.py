from xmlrpc.server import SimpleXMLRPCServer
from copy import deepcopy
from typing import Tuple
import threading as th
import time


missed = (-1, 1, 6, 0)
valid = (2, 3, 4, 5)
maps = []
players = []
winner = -1
turn = 0
TAM = 14


def next(value=turn) -> int:
    return (value + 1) % 2


def get_turn() -> int:
    return turn


def get_winner() -> int:
    return winner


def get_players()-> int:
    return len(players)


def set_turn(value: int) -> int:
    global turn
    turn = value
    return turn


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


def print_map(matrix: list):
    for k in range(1, TAM - 1):
        print(matrix[k])


def set_poss(player, siz, poss, orientation) -> bool:
    print('Player: ', player)
    print('Tamanho da embarcação: ', siz)
    print('Posição: ', poss)
    print('Orientação ', orientation)

    length = (poss[0] - 1, poss[0] + siz)
    width = (poss[1] - 1, poss[1] + 3)

    if orientation == 'V':
        length, width = width, length

    print_map(maps[player])
    for i in range(width[0], width[1]):
        for j in range(length[0], length[1]):
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


def ready(player: int) -> str:
    global players
    players[player] = True
    if len(players) == 2:
        if players[0] and players[1]:
            return 'Jogadores prontos'

    print('Jogador ', player + 1, ' esta pronto.')
    return 'Aguardando o outro jogador...'


def login() -> int:
    global players
    if len(players) < 2:
        players.append(False)
        return len(players) - 1

    return -1


def waiting() -> bool:
    global players
    if len(players) == 2:
        if players[0] and players[1]:
            return True

    return False


def get_opponent(player: int) -> list:
    opp = next(player)
    return maps[opp]


def get_maps(login: int) -> [list, list]:
    atk = next(login)
    return maps[atk], maps[login]


def played(login: int, poss: list) -> bool:
    global maps
    atk = next(login)

    print(maps[atk][poss[0]][poss[1]])
    shot = maps[atk][poss[0]][poss[1]]
    if shot in missed:
        if shot == 0:
            maps[atk][poss[0]][poss[1]] = 1
        return False, maps[atk], maps[login]

    maps[atk][poss[0]][poss[1]] = 6
    return True, maps[atk], maps[login]


def check_winner(login: int) -> bool:
    global winner

    atk = next(login)
    for line in maps[atk]:
        for block in line:
            if block in valid:
                return False

    print('Vencedor: jogador', login + 1)
    winner = login
    return True


def reset() -> bool:
    global maps, players, winner, turn
    maps = init_maps()
    players = []
    winner = -1
    turn = 0
    return True


def register(server: SimpleXMLRPCServer):
    server.register_function(login)
    server.register_function(set_poss)
    server.register_function(ready)
    server.register_function(waiting)
    server.register_function(get_opponent)
    server.register_function(get_maps)
    server.register_function(get_winner)
    server.register_function(get_players)
    server.register_function(get_turn)
    server.register_function(set_turn)
    server.register_function(next)
    server.register_function(played)
    server.register_function(check_winner)
    server.register_function(reset)


def main():
    print('Server init...')
    server = SimpleXMLRPCServer(('0.0.0.0', 9999))

    register(server)

    print('Ctrl + C to end')
    server.serve_forever()


if __name__ == '__main__':
    maps = init_maps()
    main()
