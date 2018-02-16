# -*- coding: utf-8 -*-
from msvcrt import getch
from os import system


def regras():
    print('Regras do jogo \n')

    print(' Armas disponíveis: ')
    print('   - 4 Subimarinos  [ ][ ]')
    print('   - 3 Cruzadores   [ ][ ][ ]')
    print('   - 2 Encouraçados [ ][ ][ ][ ]')
    print('   - 1 Porta-aviões [ ][ ][ ][ ][ ] \n')

    print(' Tabuleiro: ')
    print('   São duas grelhas para cada jogador.')
    print('   Uma que representa a disposição dos barcos do jogador, e outra que representa a do oponente. ')
    print('   As grelhas são quadradas(10 x 10), estando identificadas na horizontal por números e na vertical'
          ' por letras. \n')

    print(' Preparação: ')
    print('   - Você distribui seus navios pelo tabuleiro. Podem ser marcado em linha horizontais ou verticais.')
    print('   - Não é permitido que 2 navios se toquem. \n')

    print(' Jogando: ')
    print('   - Disparará 3 tiros, indicando a coordenadas do alvo através da letra da linha e do '
          'número da coluna que definem a posição, segundo o exemplo. Ex: A-1.')
    print('   - Após cada um dos tiros, o jogo avisará se acertou e, nesse caso, qual a arma foi '
          'atingida. Se ela for afundada, esse fato também deverá ser informado.')
    print('   - Uma arma é afundada quando todas as casas que formam essa arma forem atingidas.')
    print('   - O jogo termina quando um dos jogadores afundar todas as armas do seu oponente. \n')

    print('\n Pressione qualquer tecla para voltar ao menu ...')
    getch()


def play():
    print()


def creditos():

    print('\n Pressione qualquer tecla para voltar ao menu ...')
    getch()


def menu(se):
    menu = ['Iniciar', 'Regras', 'Creditos']
    i = 0

    print('\n', ' ' * 1, '** Batalha Naval v1.0 **\n')
    print('// ', '-' * 23, ' \\\ \n')

    while i < len(menu):
        if se == i:
            print(' ' * 8, '[>] ', menu[i], ' \n')
        else:
            print(' ' * 8, '[ ] ', menu[i], ' \n')

        i += 1

    print('\\\ ', '-' * 23, ' // \n')
    print('*Pressione ESC para fechar ')


def intera(init=0, final=2, se=0):
    options = {0: play,
               1: regras,
               2: creditos, }

    key = 0
    while key != 27:
        system('cls')
        menu(se)
        key = int(ord(getch()))
        system('cls')

        if key == 119:
            if se <= init:
                se = final
            else:
                se -= 1
        if key == 115:
            if se >= final:
                se = init
            else:
                se += 1

        if key == 13:
            options[se]()


if __name__ == '__main__':
    system('cls')
    intera()
