# -*- coding: UTF-8 -*-

from msvcrt import getch
import os


num1 = 0.0
num2 = 0.0


def finale():
	print("\nPessione qualquer tecla para voltar ao menu...")
	x = getch()
	os.system('cls')
    
    
def questao01():
    # Hello, World
    print("Hello, World")
    
    finale()
	

def questao02():
    # Faça um Programa que peça um número e então
    # mostre a mensagem O número informado foi
    # [número].

    num1 = input("Digite um numero ")
    print "O numero informado foi [",num1,"]"
    
    finale()


def questao03():
    # Faça um algoritmo que receba dois números e ao
    # final mostre a soma, subtração, multiplicação e a
    # divisão dos números lidos.

    num1 = input("Digite um numero ")
    num2 = input("Digite outro ")

    print "\nSoma: ", num1 + num2
    print "Subtracao: ", num1 - num2
    print "Multiplicacao: ", num1 * num2
    print "Divisao: ", num1 / num2
    
    finale()


def questao04():
    # Faça um Programa que converta metros para centímetros

    num1 = input("Digite uma medita em metros ")
    print num1 * 100, " cm"
    
    finale()


def questao05():
    # Faça um Programa que pergunte quanto você ganha por hora e
    # o número de horas trabalhadas no mês. Calcule e mostre o total
    # do seu salário no referido mês.

    valorHora = 0.0
    horasMes = 0
    valorHora = input("Quanto voce ganha por hora? ")
    horasMes = input("Quantas horas você traballhou nesse mes? ")

    print "Seu Salario nesse referido mes foi R$ %.2f"%(valorHora * horasMes)
    
    finale()


def questao06():
    # Quantas milhas há em 10 quilômetros?

    print "Em 10 Km ha ", 10 / 1.60934, " M"
    
    finale()


def questao07():
    # Escrever um algoritmo para determinar o consumo médio de
    # um automóvel sendo fornecida a distância total percorrida pelo
    # automóvel e o total de combustível gasto.

    num1 = input("Digite a distancia total percorrida ")
    num2 = input("Digite o total de combustivel gasto ")

    print "Consumo médio:  ", num1 / num2
    
    finale()


def questao08():
    # Elaborar um algoritmo que efetue a apresentação do valor da
    # conversão em real (R$) de um valor lido em dólar (US$). O
    # algoritmo deverá solicitar o valor da cotação do dólar e também a
    # quantidade de dólares disponíveis com o usuário.

    num1 = input("Digita a contação do dolar ")
    num2 = input("Agora o valor em dólar há ser convertido ")

    print num2, " US$ equivale ha ", num2 * num1, " R$" 
    
    finale()


def questao09():
    # Escreva um algoritmo que leia um número inteiro positivo e exiba o dobro do mesmo

    num = 0
    num = input("Digite um numero inteiro positivo")

    if (num < 0):
        print("O numero nao e positivo, tente novamente")
    else :
        print(num * 2, "e o dobro de ", num)    
        
    finale()


def questao10():
    # Escreva um algoritmo para calcular e exibir a média ponderada de 2
    # notas dadas. Utilize constantes nos pesos. (nota1= peso 6 e nota2= peso 4)

    nota1 = 6
    nota2 = 4

    num1 = input("Primeira nota ")
    num2 = input("Segunda nota ")
    media = ((num1*nota1)+(num2*nota2))/(nota1+nota2)

    print "Media: ", media
    
    finale()


def questao11():
    # Escreva um algoritmo para calcular e exibir o comprimento de uma
    # circunferência, sendo dada o valor de seu raio ( (∏R2)

    num1 = input("Informe o raio ")
    print "circunferência de raio ", num1, "equivale há ", 3.1415*num1**2 
    
    finale()


def questao12():
    # Escreva um algoritmo para ler uma temperatura dada na escala
    # Fahrenheit (F) e exibir o equivalente em Celsius (C ) [ C = (5 * (F-32) /9)].

    F = 0.0
    F = input("Digite uma temperatura em F")
    C = (5 * (F - 32) / 9)
    print F, "Fahrenheit = ", C, " Celsius" 
    
    finale()


def questao13():
    # Escreva um algoritmo para calcular a área de um triângulo equilátero,
    # sendo dados a sua base (b) e a sua altura (h) [ fórmula= (b*h)/2].

    b = h = 0.0

    b = input("Informe a base")
    h = input("Agora a altura")
    formula = (b*h)/2

    print "Área do triângulo de base ", b, "e altura ", h, "é: ", formula 
    
    finale()


def questao14():
    # Escreva um algoritmo que leia duas variáveis inteiras e troque o
    # conteúdo entre elas.

    var1 = var2 = var3 = 0
    var1 = input("Primeira variável ")
    var2 = input("Segunda variável ")

    var3 = var1
    var1 = var2
    var2 = var3

    print "Primeira variável: ", var1
    print "Segunda variável: ", var2
    
    finale()


init = 1
final = 14
se = 1

def menu(se):
	i = 1;
	print ("// ------------------------------- \\\ \n")

	while (i <= final):
		if (se == i):
			print "      [>] ========= Questao ", i, "\n"
		else:
			print "      [ ] ========= Questao ", i, "\n"
		i+= 1
				
	print ("\\\ ------------------------------- // \n")

options = {1 : questao01,
           2 : questao02,
           3 : questao03,
           4 : questao04,
           5 : questao05,
           6 : questao06,
           7 : questao07,
           8 : questao08,
           9 : questao09,
           10 : questao10,
           11 : questao11,
           12 : questao12,
           13 : questao13,
           14 : questao14,}

key = 0
while key != 27:
	menu(se)
	key = int(ord(getch()))
	os.system('cls')
	
	if(key == 119):
		if(se <= init):
			se = final
		else:
			se-= 1
	if(key == 115):
		if(se >= final):
			se = init
		else:
			se+= 1
			
	if(key == 13):
		options[se]()
