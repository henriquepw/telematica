from xmlrpc.server import SimpleXMLRPCServer
from copy import deepcopy


map_player1 = []
map_player2 = []
TAM = 14


# 12 X 12 com bordas
def init_maps():
    player1 = [[-1 for _ in range(TAM)]]

    for _ in range(1, 13):
        line = [-1]
        line += [0 for _ in range(TAM - 2)]
        line.append(-1)
        player1.append(line)

    player1.append([-1 for _ in range(TAM)])
    player2 = deepcopy(player1)
    return player1, player2


def is_valid():
    pass


def fill_map():
    pass


def main():
    print('Server init...')
    server = SimpleXMLRPCServer(('0.0.0.0', 9999))
    print('Ctrl + C to end')
    server.serve_forever()


if __name__ == '__main__':
    init_maps()
    main()
