# encoding: utf-8
from random import randint

from source.Sample import *
from source.cube import *

basic = {'R': r_l, 'R\'': r_l, 'R2': r_l, 'L': r_l, 'L\'': r_l, 'L2': r_l,
         'D': d_u, 'D\'': d_u, 'D2': d_u, 'U': d_u, 'U\'': d_u, 'U2': d_u,
         'F': f, 'F\'': f, 'F2': f, 'B': b, 'B\'': b, 'B2': b}

muvs = ['R', 'R\'', 'R2', 'L', 'L\'', 'L2', 'D', 'D\'', 'D2',
        'U', 'U\'', 'U2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2']


def create_examples():
    examples = open('Examples.txt', 'a')
    olds_movements = []
    repetido = False

    for e in range(1, 101):
        init()
        movements = ''
        old_r = -1

        for i in range(25):
            r = randint(0, 17)

            if r == old_r:
                i -= 1
            else:
                old_r = r
                m = muvs[r]
                movements += ' ' + m
                basic[m](m)

        for m in olds_movements:
            if movements == m:
                repetido = True
                break

        if repetido:
            e -= 1
        else:
            olds_movements.append(movements)
            print_c()

            print('Ex %d: ' % e + movements)

            examples.write('Ex %d: \n' % e)
            examples.write('Cubo: ' + str(cube) + '\n')
            examples.write('Embaralhamento: ' + movements + '\n')
            examples.write('Resolução: \n')
            examples.write('---------------- \n')

    examples.close()


def read_examples():
    exemples = open('Examples.txt', 'r')

    for i in range(100):
        ex = exemples.readline()

        sample = Sample(
            eval(exemples.readline().split(': ')[1]),
            exemples.readline().split(': ')[1],
            exemples.readline().split(': ')[1]
        )

        exemples.readline()

        print(ex)
        sample.__str__()

    exemples.close()


def main():
    while True:
        muv = input().upper()

        if muv == 'SAIR':
            break
        elif muv:
            basic[muv](muv)
            print_c()


if __name__ == '__main__':
    init()
    read_examples()
