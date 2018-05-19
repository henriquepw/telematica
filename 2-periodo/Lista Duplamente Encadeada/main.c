#include <stdio.h>
#include <stdlib.h>

typedef struct elem{
	int num;
	struct elem *ant, *prox;
} node;

typedef struct list{
	int size;
	node *init, *last;
} List;

List *createList();
node *alloc(int);
int isEmpty(List *);

void push(List *, int);
void pushFirst(List *, int);
void pushIn(List *, int);

void menu(List *);
void clean();


int main(void){
	List *alunos = createList();
	
	pushIn(alunos, 2);
	pushIn(alunos, 3);
	pushIn(alunos, 4);
	pushIn(alunos, 6);
	pushIn(alunos, 7);
	pushIn(alunos, 5);
	pushIn(alunos, 8);
	pushIn(alunos, 12);
	pushIn(alunos, 10);
	pushIn(alunos, 0);
	pushIn(alunos, 1);
	
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

node *alloc(int num){
	node *novo = (node *)malloc(sizeof(node));

	if(novo == NULL){
		printf("Nao foi possivel alocar memoria");
	} else{
		novo->num = num;
		novo->prox = NULL;
		novo->ant = NULL;
	}

	return novo;
}

int isEmpty(List *list){
  return (list->init == NULL) && (list->last == NULL);
}

void push(List *list, int num){
	node *novo = alloc(num);

	if(isEmpty(list)){
		list->init = novo;
		list->last = novo;
	} else {
		novo->ant = list->last;
		list->last->prox = novo;
		list->last = novo;
	}
	
	list->size++;

}

void pushFirst(List *list, int num){
	node *novo = alloc(num);

	if(isEmpty(list)){
		list->init = novo;
		list->last = novo;
	} else {
		novo->prox = list->init;
		list->init->ant = novo;
		list->init = novo;
	}
	
	list->size++;
}

void pushIn(List *list, int num){
  if (isEmpty(list)){
  	node *novo = alloc(num);
    list->init = novo;
    list->last = novo;
    list->size++;
    
  } else if(num < list->init->num){
    pushFirst(list, num);
    
  } else if (num > list->last->num){
    push(list, num);
    
  } else {
    node *auxI = list->init;
	node *auxL = list->last;
	
    while( (num > auxI->num) && (num < auxL->num) &&
    (auxI->prox != NULL) && (auxL->ant != NULL)){
		  auxI = auxI->prox;
		  auxL = auxL->ant;
	}
	
	node *aux;
	if(num >= auxL->num) aux = auxL;
	else aux = auxI->ant;
		
	node *novo = alloc(num);
	novo->prox = aux->prox;
	novo->ant = aux;
	aux->prox = novo; 
	aux->prox->ant = novo;
	list->size++;
  }
  
}

void showFirst(List *list){
	if(!isEmpty(list)) printf("Primeiro numero: %d \n", list->init->num);
	else printf("Lista vazia. \n");
}

void showLast(List *list){
	if(!isEmpty(list)) printf("Ultimo Numero: %d \n", list->last->num);
	else printf("Lista vazia. \n");
}

// begin 1- vai do init até last; 0- vai de last ate init
void showAll(List *list, int begin){ 
	if (begin){
		node *aux = list->init;
		while(aux != NULL){
			printf("Primeiro numero: %d \n", aux->num);
			aux = aux->prox;
		}
	} else {
		node *aux = list->last;
		while(aux != NULL){
			printf("Primeiro numero: %d \n", aux->num);
			aux = aux->ant;
		}
	}
	
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

		printf("11. Inserir no inicio \n");
		printf("12. Inserir ordenado \n");
		
		printf("00. Sair \n");
		scanf("%d", &se);
		
		int num;
		switch(se){
			case 1:
				printf("Digite o numero: ");
				scanf("%d", &num);
				push(list, num);
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
				showAll(list, 1);
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
			/*case 6:
				printf("Digite o nome do aluno: ");
				scanf(" %[^\n]s", name);
				showByName(list, name);
				clean();
				break;*/
			case 7:
				printf("Tamanho: %d \n", list->size);
				clean();
				break;
			/*case 8:
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
				break;*/
			case 11:
				printf("Digite o numero: ");
				scanf("%d", &num);
				pushFirst(list, num);
				clean();
				break;
			case 12:
				printf("Digite o numero: ");
				scanf("%d", &num);
				pushIn(list, num);
				clean();
				break;
			case 13:
				list = createList();
				clean();
				break;
			case 0:
				return;
				break;
			default:
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
