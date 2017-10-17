# Aula 3 - Conceitos importantes
# Tipos de dados, constantes, variaveis e expressoes aritmeticas

# -*- coding: utf-8 -*-
num1 = 0.0
num2 = 0.0


def questao01():
    # Hello, World

    print("Hello, World");


def questao02():
    # Faça um Programa que peça um número e então
    # mostre a mensagem O número informado foi
    # [número].

    num1 = input("Digite um numero")
    print("O número informado foi [", num1, "]")


def questao03():
    # Faça um algoritmo que receba dois números e ao
    # final mostre a soma, subtração, multiplicação e a
    # divisão dos números lidos.

    num1 = input("Digite um numero")
    num2 = input("Digite outro")

    print("Soma: ", num1 + num2)
    print("Subtração: ", num1 - num2)
    print("Multiplicação: ", num1 * num2)
    print("Divisão: ", num1 / num2)


def questao04():
    # Faça um Programa que converta metros para centímetros

    num1 = input("Digite uma medita em metros")
    print(num1 * 100, " centímetros")


def questao05():
    # Faça um Programa que pergunte quanto você ganha por hora e
    # o número de horas trabalhadas no mês. Calcule e mostre o total
    # do seu salário no referido mês.

    valorHora = 0.0
    horasMes = 0
    valorHora = input("Quanto você ganha por hora?")
    horasMes = input("Quantas horas você traballhou nesse mês?")

    print("Seu Salário nesse referido mês foi: ", valorHora * horasMes)


def questao06():
    # Quantas milhas há em 10 quilômetros?

    print("Em 10 Km há ", 10 / 1.60934, " M")


def questao07():
    # Escrever um algoritmo para determinar o consumo médio de
    # um automóvel sendo fornecida a distância total percorrida pelo
    # automóvel e o total de combustível gasto.

    num1 = input("Digite a distância total percorrida")
    num2 = input("Digite o total de combustível gastoo")

    print("Consumo médio:  ", num1 / num2)


def questao08():
    # Elaborar um algoritmo que efetue a apresentação do valor da
    # conversão em real (R$) de um valor lido em dólar (US$). O
    # algoritmo deverá solicitar o valor da cotação do dólar e também a
    # quantidade de dólares disponíveis com o usuário.

    num1 = input("Digita a contação do dólar")
    num2 = input("Agora o valor em dólar há ser convertido")

    print(num2, " US$ equivale há ", num2 * num1, " R$")


def questao09():
    # Escreva um algoritmo que leia um número inteiro positivo e exiba o dobro do mesmo

    num = 0
    num = input("Digite um numero inteiro positivo")

    if (num < 0):
        print("O número não é positivo, tente novamente")
    else :
        print(num * 2, "é o dobro de ", num)


def questao10():
    # Escreva um algoritmo para calcular e exibir a média ponderada de 2
    # notas dadas. Utilize constantes nos pesos. (nota1= peso 6 e nota2= peso 4)

    nota1 = 6
    nota2 = 4

    num1 = input("Primeira nota")
    num2 = input("Segunda nota")
    media = ((num1*nota1)+(num2*nota2))/(nota1+nota2)

    print("Media: ", media)


def questao11():
    # Escreva um algoritmo para calcular e exibir o comprimento de uma
    # circunferência, sendo dada o valor de seu raio ( (∏R2)

    num1 = input("Informe o raio")
    print("circunferência de raio ", num1, "equivale há ", 3.1415*num1**2)


def questao12():
    # Escreva um algoritmo para ler uma temperatura dada na escala
    # Fahrenheit (F) e exibir o equivalente em Celsius (C ) [ C = (5 * (F-32) /9)].

    F = 0.0
    F = input("Digite uma temperatura em F")
    C = (5 * (F - 32) / 9)
    print(F, "Fahrenheit = ", C, " Celsius")


def questao13():
    # Escreva um algoritmo para calcular a área de um triângulo equilátero,
    # sendo dados a sua base (b) e a sua altura (h) [ fórmula= (b*h)/2].

    b = h = 0.0

    b = input("Informe a base")
    h = input("Agora a altura")
    formula = (b*h)/2

    print("Área do triângulo de base ", b, "e altura ", h, "é: ", formula)


def questao14():
    # Escreva um algoritmo que leia duas variáveis inteiras e troque o
    # conteúdo entre elas.

    var1 = var2 = var3 = 0
    var1 = input("Primeira variável")
    var2 = input("Segunda variável")

    var3 = var1
    var1 = var2
    var2 = var3

    print("Primeira variável: ", var1)
    print("Segunda variável: ", var2)
