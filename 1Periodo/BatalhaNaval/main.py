# -*- coding: utf-8 -*-
from random import randint

attack = {}
defense = {}

'''

5 = 1x Porta-aviões
4 = 2x Encouraçados 
3 = 3x Cruzadores 
2 = 4x subimarinos

'''


def crange(c1, c2):
    yield from range(ord(c1), ord(c2) + 1)


def init():
    for c in crange('A', 'J'):
        attack[chr(c)] = [0 for k in range(10)]
        defense[chr(c)] = [0 for k in range(10)]

    for i in range(2, 6):
        preencher(i, 6 - i)


def preencher(tipo, quantidade):
    c = 0
    while c < quantidade:
        sentido = randint(0, 1)

        if sentido == 0:
            linha = chr(randint(ord('A'), ord('J')))
            coluna = randint(0, 10 - tipo)

            confirmed = True
            for i in range(tipo):
                if defense[linha][coluna + i] != 0:
                    confirmed = False

            if confirmed:
                for i in range(tipo):
                    defense[linha][coluna + i] = tipo
                c += 1

        else:
            linha = chr(randint(ord('A'), ord('K') - tipo))
            coluna = randint(0, 9)

            confirmed = True
            for i in range(tipo):
                if defense[chr(ord(linha) + i)][coluna] != 0:
                    confirmed = False

            if confirmed:
                for i in range(tipo):
                    defense[chr(ord(linha) + i)][coluna] = tipo
                c += 1


def bloco(bloco):
    for c in crange('A', 'J'):
        print(bloco[chr(c)])


if __name__ == '__main__':
    init()
    bloco(defense)
