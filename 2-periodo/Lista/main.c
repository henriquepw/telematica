#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM 15

typedef struct elem{
	char nome[TAM];
	char matricula[TAM];
	float media_anual;
	struct elem *prox;
} node;

typedef struct list{
	int size;
	node *init;
	node *last;
} List;

List *createList();
node *alloc();
int isEmpty(List *list);

void push(List *list);

void showAll(List *list);
void showFirst(List *list);
void showLast(List *list);
void showByName(List *list, char name[]);
void printAluno(node *aluno);

void popFirst(List *list);
void popLast(List *list);
void popByName(List *list, char name[]);

void menu(List *list);
void clean();


int main(void){
	List *alunos = createList();

	menu(alunos);
	
	return 0;
}

List *createList(){
	List *list = (List *)malloc(sizeof(List));

	list->size = 0;
	list->init = NULL;
	list->last = NULL;

	return list;
}

void push(List *list){
	node *alun = alloc();

	if(isEmpty(list)){
		list->init = alun;
		list->last = alun;
		list->size++;
	} else {
		list->last->prox = alun;
		list->last = alun;
		list->size++;
	}

}

void showAll(List *list){
	node *aux = list->init;
	int i = 1;

	if(isEmpty(list)){
		printf("Lista vazia! \n");
	} else {
		while(aux != NULL){
			printf("Dados do aluno %d \n", i);
			printAluno(aux);
			aux = aux->prox;
			i++;
		}
	}
}

void showFirst(List *list){
	printAluno(list->init);
}

void showLast(List *list){
	printAluno(list->last);
}

void showByName(List *list, char name[]){
	if(isEmpty(list)){
		printf("Lista vazia. \n");
	} else if(strcmp(list->last->nome, name) == 0){
		printAluno(list->last);
	} else {
		node *aux = list->init;
		
		while ((strcmp(aux->nome, name) != 0) && (aux->prox != list->last))
			aux = aux->prox;
			
		if(strcmp(list->last->nome, name) == 0){
			printAluno(aux);
		}else {
			printf("Aluno nao encontrado. \n");
		}
		
	}
}

void popFirst(List *list){
	if (isEmpty(list)){
		printf("Lista vazia,  nao tem item para ser removido. \n");
	} else {
		node *aux = list->init;
		list->init = list->init->prox;
		list->size--;
		free(aux);
	}	
}

void popLast(List *list){
	if (isEmpty(list)){
		printf("Lista vazia, nao tem item para ser removido. \n");
	} else if(list->size == 1){
		free(list->last);
		list->init = NULL;
		list->last = NULL;	
		list->size--;
	} else {
		node *aux = list->init;
		
		while (aux->prox != list->last){
			aux = aux->prox;
		}
		
		list->last = aux;
		free(aux->prox);
		list->last->prox = NULL;
		list->size--;
	}
}

void popByName(List *list, char name[]){
	if(isEmpty(list)){
		printf("Lista vazia \n");
		
	} else if(list->size == 1){
		free(list->init);
		list->init = NULL;
		list->last = NULL;
		list->size = 0;
		
	} else if(strcmp(list->init->nome, name) == 0){
		popFirst(list);
		
	} else if(strcmp(list->last->nome, name) == 0){
		popLast(list);
		
	} else {
		node *anterior = list->init;
		node *atual = list->init;
		
		while ((strcmp(atual->nome, name) != 0) && (atual->prox != NULL)){
			anterior = atual;
			atual = atual->prox;
		}
		
		if (strcmp(atual->nome, name) == 0){
			anterior->prox = atual->prox;
			free(atual);
			list->size--;
		} else {
			printf("Aluno nao encontrado. \n");
		}
	}
}

node *alloc(){
	node *novo = (node *)malloc(sizeof(node));

	if(novo == NULL){
		printf("N�o foi possivel alocar memoria");
	} else{
		printf("Digite os dados do novo aluno \n");

		printf(" -Nome: ");
		scanf(" %[^\n]s", novo->nome);
		printf(" -Matricula: ");
		scanf("%s", novo->matricula);
		printf(" -Media anual: ");
		scanf("%f", &novo->media_anual);
		novo->prox = NULL;
	}

	return novo;
}

void printAluno(node *aluno){
	printf(" --Nome: %s \n", aluno->nome);
	printf(" --Matricula: %s \n", aluno->matricula);
	printf(" --Media anual: %.1f\n", aluno->media_anual);
}

int isEmpty(List *list){
  return list->size == 0;
}

void menu(List *list){
	int se = -1;
	while (se != 0){
		printf("01. Inserir \n");
		printf("02. verificar se esta vazia \n");
		
		printf("03. Exibir lista \n");
		printf("04. Exibir o primeiro \n");
		printf("05. Exibir o ultimo \n");
		printf("06. Pesquisar aluno por nome \n");
		
		printf("07. Tamanho \n");
		
		printf("08. Remover o primeiro \n");
		printf("09. Remover o ultimo \n");
		printf("10. Remover aluno por nome \n");
		
		printf("00. Sair \n");
		scanf("%d", &se);
		
		char name[TAM];
		switch(se){
			case 1:
				push(list);
				clean();
				break;
			case 2:
				if(isEmpty(list))
					printf("Lista esta vazia! \n");
				else 
					printf("Lista nao esta vazia! \n");
				
				clean();
				break;
			case 3:
				showAll(list);
				clean();
				break;
			case 4:
				showFirst(list);
				clean();
				break;
			case 5:
				showLast(list);
				clean();
				break;
			case 6:
				printf("Digite o nome do aluno: ");
				scanf(" %[^\n]s", name);
				showByName(list, name);
				clean();
				break;
			case 7:
				printf("Tamanho: %d \n", list->size);
				clean();
				break;
			case 8:
				popFirst(list);
				clean();
				break;
			case 9:
				popLast(list);
				clean();
				break;
			case 10:
				printf("Digite o nome do aluno: ");
				scanf(" %[^\n]s", name);
				popByName(list, name);
				clean();
				break;
			case 0:
				puts("\x1b[H\x1b[2J");
				printf("Comando invalido. Digite novamente \n");
				break;
		}
		
	}	
}

void clean(){
	system("pause");
	puts("\x1b[H\x1b[2J");
}

