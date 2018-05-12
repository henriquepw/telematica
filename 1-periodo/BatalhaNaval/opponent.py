# encoding: utf-8
import copy
from random import randint as ri

mapa_player = []
tamanho = 12

'''

5 = 1x Porta-aviões
4 = 2x Encouraçados 
3 = 3x Cruzadores 
2 = 4x subimarinos

'''


# range de letra a letra
def crange(c1, c2):
    yield from range(ord(c1), ord(c2) + 1)


# inicia os tabulheiros
def init(tam=12):
    global tamanho
    tamanho = tam
    for c in range(tamanho):
        mapa_player.append([0 for k in range(tamanho)])

    for i in range(2, 3):
        preencher(i, 6 - i)

    return copy.deepcopy(mapa_player)


# verifica os arredores das posições dos navios
def verificar(linha, coluna, confirmed):
    global mapa_player

    if linha == tamanho - 1:
        linha_verificar = [linha - 1, linha + 1]
    elif linha == 0:
        linha_verificar = [linha, linha + 2]
    else:  # linha > 0:
        linha_verificar = [linha - 1, linha + 2]

    if coluna == tamanho - 1:
        coluna_verificar = [coluna - 1, coluna + 1]
    elif coluna == 0:
        coluna_verificar = [coluna, coluna + 2]
    else:  # coluna > 0:
        coluna_verificar = [coluna - 1, coluna + 2]

    for li in range(linha_verificar[0], linha_verificar[1]):
        for co in range(coluna_verificar[0], coluna_verificar[1]):
            if mapa_player[li][co] != 0:
                confirmed = False
                # print('entrou')
    return confirmed


# preencher de forma aleatoria segundo as regras do jogo o tabulheiro de defesa da maquina
def preencher(tipo, quantidade):
    global mapa_player
    c = 0

    while c < quantidade:
        # 0 = horizontal ; 1 = Vertical
        sentido = ri(0, 1)

        if sentido == 0:
            # aleatorizando uma posição
            linha = ri(0, tamanho - 1)
            coluna = ri(0, tamanho - tipo)

            # confirmando se a posição que foi aleatorizada está livre
            confirmed = True
            for i in range(tipo):
                confirmed = verificar(linha, coluna + i, confirmed)

                if mapa_player[linha][coluna + i] != 0:
                    confirmed = False

            # se for confirmado, preenche
            if confirmed:
                for i in range(tipo):
                    mapa_player[linha][coluna + i] = tipo
                c += 1

        else:
            linha = ri(0, tamanho - tipo)
            coluna = ri(0, tamanho - 1)

            confirmed = True
            for i in range(tipo):
                confirmed = verificar(linha + i, coluna, confirmed)

            if confirmed:
                for i in range(tipo):
                    mapa_player[linha + i][coluna] = tipo
                c += 1


# print o tabulheiro
def print_mapas(mapa1):
    line = '  '
    for x in range(tamanho):
        if x <= 9:
            line += ' 0' + str(x)
        else:
            line += ' ' + str(x)

    print(line)
    for i in range(tamanho):
        if i <= 9:
            line = '0' + str(i) + ' '
        else:
            line = '' + str(i) + ' '
        for j in range(tamanho):
            if mapa1[i][j] == 1:
                line += '\033[7;31m[X]\033[m'
            elif mapa1[i][j] == 6:
                line += '\033[7;32m[V]\033[m'
            else:
                line += '\033[7;30m[ ]\033[m'
        print(line)


def validar_hit(a, b):
    if mapa_player[a][b] == 1 or mapa_player[a][b] == 6:
        return False
    else:
        return True


def hit(a, b):
    global mapa_player
    if mapa_player[a][b] != 0 and validar_hit(a, b):
        print("Achamos um navio na posicao %dx%d, Senhor" % (a + 1, b + 1))
        mapa_player[a][b] = 6
        return True
    else:
        print("Na posicao %dx%d. Nao achamos o navio inimigo, Senhor" % (a + 1, b + 1))
        mapa_player[a][b] = 1
        return False


def verificar_sentido(sentido, a, b, tamanho):
    if a == 0:
        if b == 0:
            sentido = ri(2, 3)
        elif b == tamanho:
            while sentido == 1 or sentido == 2:
                sentido = ri(0, 3)
        elif sentido == 1:
            while sentido == 1:
                sentido = ri(0, 3)
        print("Sentido", +sentido)

    if a == tamanho:
        if b == 0:
            sentido = ri(1, 2)
        elif b == tamanho:
            sentido = ri(0, 1)
        elif sentido == 3:
            sentido = ri(0, 2)
        print("Sentido", +sentido)
    if b == 0:
        sentido = ri(1, 3)
    if b == tamanho:
        if sentido == 2:
            while sentido:
                sentido = ri(0, 3)
        print("Sentido", +sentido)
    return sentido


def enemy(mapa_ataque):
    global tamanho
    global mapa_player

    mapa_player = copy.deepcopy(mapa_ataque)

    a = ri(0, tamanho)
    b = ri(0, tamanho)

    tiro = True

    while tiro:
        if hit(a, b):
            sentido = ri(0, 3)  # 0,1,2,3 = Esquerda, cima, direita, baixo

            sentido = verificar_sentido(sentido, a, b, tamanho)

            if sentido == 0:
                for i in range(1, 6):
                    if not hit(a, b - i):
                        tiro = False
                        break
            elif sentido == 1:
                for i in range(1, 6):
                    if not hit(a - i, b):
                        tiro = False
                        break
            elif sentido == 2:
                for i in range(1, 6):
                    if not hit(a, b + i):
                        tiro = False
                        break
            else:
                for i in range(1, 6):
                    if not hit(a + i, b):
                        tiro = False
                        break

        else:
            tiro = False

    return copy.deepcopy(mapa_player)


'''
if __name__ == '__main__':
    init()
    enemy()
'''
