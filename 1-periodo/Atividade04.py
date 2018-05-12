# Feito em: 21/11/2017
# Data da entrega 23/11/2017

def questao01():
    valores = []
    maior = medio = 0.0
    for x in range(0, 3):
        valores.append(float(input("Digite o valor: ")))
        if maior < valores[x]:
            maior = valores[x]
    for x in range(0, 3):
        if medio < valores[x] < maior:
            medio = valores[x]

    print("Soma dos 2 maiores = ", maior + medio)


def questao02():
    numero = [float(x) for x in input().split(" ")]
    print("%.2f" % (numero[0]/numero[1]))
