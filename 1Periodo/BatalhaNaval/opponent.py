# encoding: utf-8
from random import randint
import copy

attack = []
defense = []
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
def init(tam):
    global tamanho
    tamanho = tam
    for c in range(tamanho):
        defense.append([0 for k in range(tamanho)])

    for i in range(2, 3):
        preencher(i, 6 - i)

    return copy.deepcopy(defense)


# verifica os arredores das posições dos navios
def verificar(linha, coluna, confirmed):
    global defense

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
            if defense[li][co] != 0:
                confirmed = False
                # print('entrou')
    return confirmed


# preencher de forma aleatoria segundo as regras do jogo o tabulheiro de defesa da maquina
def preencher(tipo, quantidade):
    global defense
    c = 0

    while c < quantidade:
        # 0 = horizontal ; 1 = Vertical
        sentido = randint(0, 1)

        if sentido == 0:
            # aleatorizando uma posição
            linha = randint(0, tamanho - 1)
            coluna = randint(0, tamanho - tipo)

            # confirmando se a posição que foi aleatorizada está livre
            confirmed = True
            for i in range(tipo):
                confirmed = verificar(linha, coluna + i, confirmed)

                if defense[linha][coluna + i] != 0:
                    confirmed = False

            # se for confirmado, preenche
            if confirmed:
                for i in range(tipo):
                    defense[linha][coluna + i] = tipo
                c += 1

        else:
            linha = randint(0, tamanho - tipo)
            coluna = randint(0, tamanho - 1)

            confirmed = True
            for i in range(tipo):
                confirmed = verificar(linha + i, coluna, confirmed)

            if confirmed:
                for i in range(tipo):
                    defense[linha + i][coluna] = tipo
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

'''
if __name__ == '__main__':
    init()
    print_mapas(defense)
'''
