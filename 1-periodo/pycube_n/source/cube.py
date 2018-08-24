# encoding: utf-8
import copy

# k -> column
# j -> line
# i -> matrix

cube = [[[0 for j in range(3)] for k in range(3)] for i in range(6)]


def init():
    global cube

    for i in range(6):
        cube[i] = [[str(i) + '.1', str(i) + '.2', str(i) + '.3'],
                   [str(i) + '.4', str(i) + '.5', str(i) + '.6'],
                   [str(i) + '.7', str(i) + '.8', str(i) + '.9']]


# Print cube
def print_c():
    global cube
    colors = [
        '\033[7;30m',  # Branco
        '\033[7;33m',  # Amarelo
        '\033[7;32m',  # Verde
        '\033[7;34m',  # Azul
        '\033[7;35m',  # Roxo
        '\033[7;31m',  # Vermelho
        '\033[m',  # clear
    ]

    print()

    i = 0
    while i < 6:
        if i == 1:
            for j in range(3):
                s = []
                for x in range(1, 4):
                    s += [
                        int(cube[x][j][0].split('.')[0]),
                        int(cube[x][j][1].split('.')[0]),
                        int(cube[x][j][2].split('.')[0]),
                        int(cube[x][j][0].split('.')[1]),
                        int(cube[x][j][1].split('.')[1]),
                        int(cube[x][j][2].split('.')[1])
                    ]

                print("{}[{}]{}{}[{}]{}{}[{}]{}  {}[{}]{}{}[{}]{}{}[{}]{}  {}[{}]{}{}[{}]{}{}[{}]{}".format(
                    colors[s[0]], s[3], colors[6],
                    colors[s[1]], s[4], colors[6],
                    colors[s[2]], s[5], colors[6],
                    colors[s[6]], s[9], colors[6],
                    colors[s[7]], s[10], colors[6],
                    colors[s[8]], s[11], colors[6],
                    colors[s[12]], s[15], colors[6],
                    colors[s[13]], s[16], colors[6],
                    colors[s[14]], s[17], colors[6]
                ))

            i = 4
        else:
            for j in range(3):
                s = [
                    int(cube[i][j][0].split('.')[0]),
                    int(cube[i][j][1].split('.')[0]),
                    int(cube[i][j][2].split('.')[0]),
                    int(cube[i][j][0].split('.')[1]),
                    int(cube[i][j][1].split('.')[1]),
                    int(cube[i][j][2].split('.')[1])
                ]
                print("           {}[{}]{}{}[{}]{}{}[{}]{}".format(colors[s[0]], s[3], colors[6],
                                                                   colors[s[1]], s[4], colors[6],
                                                                   colors[s[2]], s[5], colors[6]))

            i += 1

        print()
    print('  -------------------------')


def r_l(arg='R'):
    global cube

    # Os movimento da direita e esquerda é o mesmo codigo, só muda os indices
    if arg == 'R':
        conts = [0, 3, 2, 1, 2, 1]
        cube[3] = rotate(cube[3])
    elif arg == 'L':
        conts = [2, 1, 0, 3, 0, 1]
        cube[1] = rotate(cube[1])
    elif arg == 'L\'':
        conts = [0, 3, 2, 1, 0, 1]
        cube[1] = rotate_(cube[1])
    elif arg == 'R\'':
        conts = [2, 1, 0, 3, 2, 1]
        cube[3] = rotate_(cube[3])
    elif arg == 'R2':
        conts = [0, 3, 2, 1, 2, 2]
        cube[3] = rotate(cube[3])
        cube[3] = rotate(cube[3])
    else:  # arg == 'L2':
        conts = [2, 1, 0, 3, 0, 2]
        cube[1] = rotate(cube[1])
        cube[1] = rotate(cube[1])

    for a in range(conts[5]):
        column = []

        # Pega os lados do cubo que vão ser alterados
        for i in range(6):
            if i != 3 and i != 1:
                column.append([cube[i][j][conts[4]] for j in range(3)])

        # Faz o movimento
        for j in range(3):
            cube[5][j][conts[4]] = column[conts[0]][j]
            cube[4][j][conts[4]] = column[conts[1]][j]
            cube[2][j][conts[4]] = column[conts[2]][j]
            cube[0][j][conts[4]] = column[conts[3]][j]


def f(arg='F'):
    global cube

    if arg == 'F':
        conts = [1, 0, 2, 3, 1]
        cube[2] = rotate(cube[2])
    elif arg == 'F\'':
        conts = [2, 3, 1, 0, 1]
        cube[2] = rotate_(cube[2])
    else:  # arg == 'F2'
        conts = [1, 0, 2, 3, 2]
        cube[2] = rotate(cube[2])
        cube[2] = rotate(cube[2])

    for a in range(conts[4]):
        column = [[], [], [], []]
        for j in range(3):
            column[0].append(cube[0][2][j])
            column[1].append(cube[1][j][2])
            column[2].append(cube[3][j][0])
            column[3].append(cube[4][0][j])

        for j in range(3):
            if arg == 'F\'':
                c = [j * 2, 2]
            else:
                c = [2, j * 2]

            cube[0][2][j] = column[conts[0]][c[0] - j]
            cube[3][j][0] = column[conts[1]][c[1] - j]
            cube[4][0][j] = column[conts[2]][c[0] - j]
            cube[1][j][2] = column[conts[3]][c[1] - j]


def b(arg='B'):
    global cube

    if arg == 'B':
        conts = [2, 3, 1, 0, 1]
        cube[5] = rotate(cube[5])
    elif arg == 'B\'':
        conts = [1, 0, 2, 3, 1]
        cube[5] = rotate_(cube[5])
    else:  # arg == 'B2'
        conts = [2, 3, 1, 0, 2]
        cube[5] = rotate(cube[5])
        cube[5] = rotate(cube[5])

    for a in range(conts[4]):
        column = [[], [], [], []]
        for j in range(3):
            column[0].append(cube[0][0][j])
            column[1].append(cube[1][j][0])
            column[2].append(cube[3][j][2])
            column[3].append(cube[4][2][j])

        for j in range(3):
            if arg == 'B':
                c = [j * 2, 2]
            else:
                c = [2, j * 2]

            cube[0][0][j] = column[conts[0]][c[0] - j]
            cube[3][j][2] = column[conts[1]][c[1] - j]
            cube[4][2][j] = column[conts[2]][c[0] - j]
            cube[1][j][0] = column[conts[3]][c[1] - j]


def d_u(arg='U'):
    global cube

    if arg == 'U':
        conts = [1, 2, 3, 0, 0, 2, 1]
        cube[0] = rotate(cube[0])
    elif arg == 'U\'':
        conts = [3, 0, 1, 2, 0, 2, 1]
        cube[0] = rotate_(cube[0])
    elif arg == 'D\'':
        conts = [1, 2, 3, 0, 2, 0, 1]
        cube[4] = rotate_(cube[4])
    elif arg == 'D':
        conts = [3, 0, 1, 2, 2, 0, 1]
        cube[4] = rotate(cube[4])
    elif arg == 'D2':
        conts = [3, 0, 1, 2, 2, 0, 2]
        cube[4] = rotate(cube[4])
        cube[4] = rotate(cube[4])
    else:  # arg == 'U2'
        conts = [1, 2, 3, 0, 0, 2, 2]
        cube[0] = rotate(cube[0])
        cube[0] = rotate(cube[0])

    for a in range(conts[6]):
        line = []
        for i in range(1, 6):
            if i == 5:
                c = [conts[5], [2, -1, -1]]
            else:
                c = [conts[4], [3]]

            if i != 4:
                line.append([cube[i][c[0]][j] for j in range(*c[1])])

        for k in range(3):
            cube[1][conts[4]][k] = line[conts[0]][k]
            cube[2][conts[4]][k] = line[conts[1]][k]
            cube[3][conts[4]][k] = line[conts[2]][k]
            cube[5][conts[5]][k] = line[conts[3]][2 - k]


def print_m(matrix):
    print()
    for j in range(3):
        print([matrix[j][k] for k in range(3)])
    print()


# Roda um lado do cubo no sentido horário
def rotate(matrix):
    matrix_aux = copy.deepcopy(matrix)

    c = 1
    for k in range(3):
        matrix[k][2] = matrix_aux[0][k]
        if k > 0:
            matrix[2][c] = matrix_aux[k][2]
            matrix[c][0] = matrix_aux[2][c]
            c -= 1

        matrix[0][1] = matrix_aux[1][0]

    return copy.deepcopy(matrix)


# Roda um lado do cubo no sentido anti-horário
def rotate_(matrix):
    matrix_aux = copy.deepcopy(matrix)

    c = 1
    for k in range(3):
        matrix[0][k] = matrix_aux[k][2]
        if k > 0:
            matrix[k][2] = matrix_aux[2][c]
            matrix[2][c] = matrix_aux[c][0]
            c -= 1

        matrix[1][0] = matrix_aux[0][1]

    return copy.deepcopy(matrix)
