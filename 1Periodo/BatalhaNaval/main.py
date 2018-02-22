import copy
from msvcrt import getch
from os import system
import opponent

# variaveis
# padrão ANSI
clear = '\033[m'
destaque = '\033[1;33m'

tamanho = 10
letra = []
sequencia = []

a = ord('A')
for l in range(tamanho):
    letra.append(chr(a + l))
    sequencia.append(l)

mapa = []
mapa_jogador = [[0 for i in range(tamanho)] for j in range(tamanho)]
mapa_maquina = opponent.init()


def regras():
    print(destaque, 'Regras do jogo \n', clear)

    print(destaque, ' Armas disponíveis: ', clear)
    print('    - 4 Subimarinos  [ ][ ]')
    print('    - 3 Cruzadores   [ ][ ][ ]')
    print('    - 2 Encouraçados [ ][ ][ ][ ]')
    print('    - 1 Porta-aviões [ ][ ][ ][ ][ ] \n')

    print(destaque, ' Tabuleiro: ', clear)
    print('    - São duas grelhas para cada jogador.')
    print('    - Uma que representa a disposição dos barcos do jogador, e outra que representa a do oponente. ')
    print('    - As grelhas são quadradas(12 x 12), estando identificadas na horizontal por números e na vertical'
          ' por letras. \n')

    print(destaque, ' Preparação: ', clear)
    print('    - Você distribui seus navios pelo tabuleiro. Podem ser marcado em linha horizontais ou verticais.')
    print('    - Não é permitido que 2 navios se toquem. \n')

    print(destaque, ' Jogando: ', clear)
    print('    - Disparará 3 tiros, indicando a coordenadas do alvo através da letra da linha e do '
          'número da coluna que definem a posição, segundo o exemplo. Ex: A-1.')
    print('    - Após cada um dos tiros, o jogo avisará se acertou e, nesse caso, qual a arma foi '
          'atingida. Se ela for afundada, esse fato também deverá ser informado.')
    print('    - Uma arma é afundada quando todas as casas que formam essa arma forem atingidas.')
    print('    - O jogo termina quando um dos jogadores afundar todas as armas do seu oponente. \n')

    print(destaque, '\nPressione qualquer tecla para voltar ao menu ...', clear)
    getch()


def creditos():
    print(destaque, 'Creditos: ', clear)
    print('  - Antonio D. S. C. Junior')
    print('  - Henrique M. Miranda')
    print('  - Henrique M. Miranda')
    print(destaque, '\nPressione qualquer tecla para voltar ao menu ...', clear)
    getch()


def menu(se):
    men = ['Iniciar', 'Regras', 'Créditos']
    i = 0

    print(destaque, '\n', ' ' * 1, '** Batalha Naval v1.0 **\n', clear)
    print('// ', '-' * 23, ' \\\ \n')

    while i < len(men):
        if se == i:
            print(' ' * 8, '[\033[1;33m>\033[m] ', men[i], ' \n')
        else:
            print(' ' * 8, '[ ] ', men[i], ' \n')

        i += 1

    print('\\\ ', '-' * 23, ' // \n')
    print(destaque, '*W: pra subir', clear)
    print(destaque, '*S: pra descer', clear)
    print(destaque, '*Pressione ESC para fechar ', clear)


# interação
def intera(init=0, final=2, se=0):
    options = {0: main,
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


# feito por junior

def imprime_mapa(mapa):
    for i in range(tamanho):
        print(mapa[i])

    return mapa


# novo print
def print_mapas(mapa1):
    print(' Ataque x Defesa')
    line = ' '
    for x in range(tamanho):
        if x <= 9:
            line += ' 0' + str(x)
        else:
            line += ' ' + str(x)

    print(line)
    for i in range(tamanho):
        line = '' + letra[i] + ' '

        for j in range(tamanho):
            if mapa1[i][j] == 1:
                line += '\033[7;31m[X]\033[m'
            elif mapa1[i][j] == 6:
                line += '\033[7;32m[V]\033[m'
            else:
                line += '\033[7;30m[ ]\033[m'

        '''
        line += ' | '

        for j in range(tamanho):
            if mapa2[i][j] == 1:
                line += '\033[7;31m[X]\033[m'
            elif mapa2[i][j] == 6:
                line += '\033[7;32m[V]\033[m'
            else:
                line += '\033[7;30m[ ]\033[m' '''
        print(line)


def posiciona_navio(mapa, navio, sentido, x, y):
    if sentido == "h":
        for i in range(navio):
            mapa[x][y + i] = navio
    elif sentido == "v":
        for i in range(navio):
            mapa[x + i][y] = navio
    return mapa


def player_posiciona_navio(mapa, embarcacoes):
    for navio in range(2, 6):

        for n in range(1):  # 6 - navio
            validador = False
            while not validador:
                system('cls')
                imprime_mapa(mapa)
                print("\nPosicionando o : " + embarcacoes[navio - 2])

                x, y = recebe_coordenada()
                sentido = h_ou_v()

                validador = verifica(mapa, navio, x, y, sentido)

                if not validador:
                    print("Nao pode colocar o navio neste local.\nTente coloca-lo em outro lugar do mapa.")
                    input("Aperte enter para prosseguir")

            mapa = posiciona_navio(mapa, navio, sentido, x, y)

    imprime_mapa(mapa)
    input("Navios posicionado com sucesso. Aperte enter para continuar")
    return mapa


def verifica(mapa, navio, x, y, sentido):
    if sentido == "h" and y + navio > 10:
        return False
    elif sentido == "v" and x + navio > 10:
        return False
    else:
        if sentido == "h":
            for i in range(navio):
                if mapa[x][y + i] != 0:
                    return False
        elif sentido == "v":
            for i in range(navio):
                if mapa[x + i][y] != 0:
                    return False
    return True


def h_ou_v():
    while True:
        var = input("Escolha horizontal (h) ou vertical (v): ").lower()
        if var == "h" or var == "v":
            return var
        else:
            print("Escolha invalida, Tente h para horizontal ou v para vertical")


def recebe_coordenada():
    while True:
        while True:
            y = input("Escolha a coluna no intervalo de 0-%d: "%(tamanho-1))
            if y.isdigit():
                y = int(y)
                break
            else:
                print('Digite apenas digitos')

        x = input("Escolha a linha no intervalo A-J: ").upper()

        if all(z != y for z in sequencia):
            print("Coordenada Y invalida tente novamente.")
        elif all(z != x for z in letra):
            print("Coordenada X invalida tente novamente.")
        else:
            for num in range(len(letra)):
                if x == letra[num]:
                    x2 = num
                    break
            return x2, y


def vencedor(mapa):
    for i in range(10):
        for j in range(10):
            if mapa[i][j] != 0 and mapa[i][j] != "*" and mapa[i][j] != "#":
                return False
    return True


def que_tiro_foi_esse(mapa, x, y):
    if mapa[x][y] == "A":
        navio = "Porta Avioes"
    elif mapa[x][y] == "B":
        navio = "Encouraçado"
    elif mapa[x][y] == "S":
        navio = "Submarino"
    elif mapa[x][y] == "D":
        navio = "Cruzados"

    mapa[-1][navio] -= 1
    if mapa[-1][navio] == 0:
        print(navio + " atingido")


def movimento(mapa, x, y):
    if mapa[x][y] == 0:
        return "Errou!"
    elif mapa[x][y] == '*' or mapa[x][y] == "#":
        return "Tente Novamente"
    else:
        return "Acertou!"


def player_atirando(mapa):
    while True:
        x, y = recebe_coordenada()
        mov = movimento(mapa, x, y)
        if mov == "Acertou!":
            print("Atingiu " + str(x) + "," + str(y))
            que_tiro_foi_esse(mapa, x, y)
            mapa[x][y] = "#"
            if vencedor(mapa):
                return "VITORIA"
        elif mov == "Errou!":
            print("O tiro " + str(x) + "," + str(y) + " nao atingiu nenhum alvo.")

        if mov != "Tente Novamente":
            return mapa


def main():
    # tipos de navios
    navios = ['Subimarinos',
              'Cruzadores',
              'Encouraçados',
              'Porta-aviões']

    # setando um mapa
    mapa = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(0)
        mapa.append(linha)

    # setando player/maquina
    mapa_jogador = copy.deepcopy(mapa)

    # adicionando navios
    # mapa_jogador.append(copy.deepcopy(navios))

    # posicionando navios
    mapa_jogador = player_posiciona_navio(mapa_jogador, navios)

    # loop principal do jogo
    while 1:

        # movimento do jogador
        print_mapas(mapa_maquina)
        mapa_maquina = player_atirando(mapa_maquina)

        # verifica se player ganhou
        if mapa_maquina == "VITORIA":
            print("Jogador vendeu!!")
            quit()

            # exibe o mapa do maquina atual
            print_mapas(mapa_maquina)
        input("Pressione enter para finalizar a jogada")

        '''
        computer move
        felipe tem que colocar aqui a jogada da maquina
        mapa_jogador = maquina_atirando(mapa_jogador)
        '''

        # verifica a jogada da maquina
        if mapa_jogador == "VITORIA":
            print("A Maquina VENCEU!!!")
            quit()

        # exibe o mapa do jogador atual
        print_mapas(mapa_jogador)
        input("Para finalizar o turno da maquina pressione ENTER")


if __name__ == '__main__':
    system('cls')
    main()
    # intera()
