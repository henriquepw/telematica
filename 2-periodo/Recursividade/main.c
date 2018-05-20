#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void q1();
int lerZero(int *);
int ler0(int *, int );

void q2();
int contido(int *, int, int);

void q3();
char *printInverso(char *, int, int);

void q4();
int palindromo(char *, int, int);

void q5();
int strSize(char *, int);

void q6();
void q7();
void q8();
void q9();
void q10();
void main(){
	/*
	q1();
	q2();
	q3();
	q4();
	*/
	
	q5();
}

void q1(){
	int vetor[] = {9, 8, 32, 3, 4, 0, 6, 7, 8, 9};
	
	printf("Index: %d \n", lerZero(vetor));
	printf("Index: %d \n", ler0(vetor, 0));
	system("pause");
}

int lerZero(int vetor[]){
	for (int i=0; i < sizeof(vetor); i++)
		if (vetor[i] == 0) return i;
	
	return -1;
}

int ler0(int vetor[], int index){
	if (index >= sizeof(vetor)) return -1;
	else if (vetor[index] == 0) return index;
	else ler0(vetor, index+1);
}

void q2(){
	int vetor[] = {9, 8, 32, 3, 4, 0, 6, 7, 8, 9};
	int comparar;
	
	scanf("%d", &comparar);
	printf("Index: %d \n", contido(vetor, comparar, 0));
	system("pause");
}

int contido(int vetor[], int comparar, int index){
	if (index >= sizeof(vetor)) return -1;
	else if (vetor[index] == comparar) return index;
	else contido(vetor, comparar, index+1);
}

void q3(){
	char vetor[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
	char vetor2[] = "0123456789";
	
	printf("Vetor: %s \n", printInverso(vetor, 0, strlen(vetor)-1));
	printf("Vetor: %s \n", printInverso(vetor2, 0, strlen(vetor)-1));
}

char *printInverso(char vetor[], int init, int last){
	if (init >= last) return vetor;
	else {
		char aux = vetor[init];
		vetor[init] = vetor[last];
		vetor[last] = aux;
		printInverso(vetor, init+1, last-1);
	}
}

void q4(){
	char frase[100];
	scanf(" %[^\n]s", frase);
	
	printf("%d", palindromo(frase, 0, strlen(frase)-1) );
}

int palindromo(char frase[], int init, int last){
	if (init >= last) return 1;
	else if (frase[init] != frase[last]) return 0;
	else palindromo(frase, init+1, last-1);
}

void q5(){
	char frase[100];
	scanf(" %[^\n]s", frase);
	
	printf("%d", strSize(frase, 0));
}

int strSize(char frase[], int index){
	if ((frase[index] == '\n') || (frase[index] == '\0')) return index;
	else strSize(frase, index+1);	
}
