from random import randint as ri

map = [[0, 2, 2, 0, 0, 0, 3, 3, 3, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [5, 5, 5, 5, 5, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 4, 4, 4, 4, 0],
       [3, 3, 3, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 4, 0, 0, 0, 0],
       [2, 0, 0, 0, 0, 4, 0, 2, 0, 3],
       [2, 0, 2, 2, 0, 4, 0, 2, 0, 3],
       [0, 0, 0, 0, 0, 4, 0, 0, 0, 3]]

tamanho = 12

def print_map():
    for i in range(len(map)):
        print(i + 1, " ", map[i])


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

enemy()
print ("10")
print_map()
