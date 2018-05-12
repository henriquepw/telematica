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


int size_n(node *aluno);
void clean(void);

void showAll(node *aluno);
void showByName(node *aluno, char name[]);
void showfirst(node *aluno);
void showLast(node *aluno);

node *removeFirst(node *aluno);
node *removeLast(node *aluno);
node *removeByName(node *aluno, char name[]);

node *getLast(node *aluno);
node *alloc(void);
node *insert(node *aluno);

void menu(node *aluno);
void print_aluno(node *aluno);
int empty(node *aux);

int main(void) {
	node *aluno = NULL;

	menu(aluno);
  
	return 0;
}

void menu (node *aluno){
  char se = -1;
  while(se != 0){
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
				aluno = insert(aluno);
				clean();
				break;
			case 2:
				if(empty(aluno)) {
				  printf("Fila vazia \n");
				} else {
				  printf("Fila nao esta vazia \n");
				}
				clean();
				break;
			case 3:
				showAll(aluno);
				clean();
				break;
			case 4:
				showfirst(aluno);
				clean();
				break;
			case 5:
				showLast(aluno);
				clean();
				break;
			case 6:
				printf("Digite o nome do aluno: ");
				scanf("%s", name);
		
				showByName(aluno, name);
				clean();
				break;
			case 7:
				printf("Tamanho da lista: %d \n", size_n(aluno));
				clean();
				break;
			case 8:
				removeFirst(aluno);
				clean();
				break;
			case 9:
				aluno = removeLast(aluno);
				clean();
				break;
			case 10:
				
				clean();
				break;
			case 0:
				
				break;
			default:
				printf("Comando nao conhecido. \n");
				clean();
				break;	
		}	
	}
}

node *insert(node *aluno){
	node *novo = alloc();
	node *aux = NULL;
	
	if (empty(aluno)){
		aluno = novo;
	}else {
		aux = getLast(aluno);
		aux->prox = novo;
	}
	
	return aluno;	
}

node *getLast(node *aluno){
	node *aux = aluno;
	
	while(aux->prox != NULL){
		aux = aux->prox;
	}
	
	return aux;
}

node *alloc(void){
	node *novo = (node *)malloc(sizeof(node));
	
	if(novo == NULL){
		printf("Não foi possivel alocar memoria");
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

void showAll(node *aluno){
	node *aux = aluno;
	int tam = 1;
	
	if(empty(aux)){
		printf("Nao tem alunos na lista. \n");
	} else {
		while (aux != NULL){
			printf("Dados do aluno %d: \n", tam);
			print_aluno(aux);
		
			aux = aux->prox;
			tam++;
		}
	}
}

void showfirst(node *aluno){
	print_aluno(aluno);
}

void showLast(node *aluno){
	node *aux = getLast(aluno);
	print_aluno(aux);
}

void showByName(node *aluno, char name[]){
	node *aux = aluno;
	while ((strcmp(aux->nome, name) != 0) && (aux->prox != NULL)){
		aux = aux->prox;
	}
	
	if(strcmp(aux->nome, name) == 0){
		print_aluno(aux);
	} else {
		printf("Aluno nao encontrado na lista! \n");
	}
}

node *removeFirst(node *aluno){
	node *aux = aluno;
	aluno = aluno->prox;
	
	free(aux);
	return aluno;
}

node *removeLast(node *aluno){
	node *aux = getLast(aluno);
	
	free(aux);	
	return aluno;
}

node *removeByName(node *aluno, char name[]){
	
	return NULL;
}

void print_aluno(node *aluno){
	printf(" --Nome: %s \n", aluno->nome);
	printf(" --Matricula: %s \n", aluno->matricula);
	printf(" --Media anual: %.1f\n", aluno->media_anual);
}

int size_n(node *aluno){
	node *aux = aluno;
	int siz = 0;
	
	while(aux != NULL){
		aux = aux->prox;
		siz++;
	}
	
	return siz;
}

int empty(node *aux){
  return aux == NULL;
}

void clean(void){
	system("pause");
	puts("\x1b[H\x1b[2J");

}


