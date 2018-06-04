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
void options();

void push(List *, int);
void pushFirst(List *, int);
void pushIn(List *, int);

void popIn(List *, int);
void popFirst(List *);
void pop(List *);
void popIndex(List *, int);
void popAll(List *);

void menu(List *);
void clean();


int main(void){
	List *alunos = createList();

	for(int i=0; i < 10; i++)
		pushIn(alunos, i);

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
    node *auxI = list->init->prox;
	node *auxL = list->last->ant;

    while( (num >= auxI->num) && (num <= auxL->num) ){
		  auxI = auxI->prox;
		  auxL = auxL->ant;
	}

	node *aux;
	if(num >= auxL->num) aux = auxL;
	else aux = auxI->ant;

	node *novo = alloc(num);
	novo->prox = aux->prox;
	novo->ant = aux;
	aux->prox->ant = novo;
	aux->prox = novo;
	list->size++;
  }

}

void pop(List *list){
	if(isEmpty(list)){
		printf("Nao existe item para ser removido");
	} else if (list->init == list->last){
		free(list->init);
		list->last = NULL;
		list->init = NULL;
		list->size--;
	}  else {
		node *aux = list->last;
		list->last = list->last->ant;
		list->last->prox = NULL;
		list->size--;
		free(aux);
	}
}

void popFirst(List *list){
	if(isEmpty(list)){
		printf("Nao existe item para ser removido");
	} else if (list->init == list->last){
		free(list->init);
		list->last = NULL;
		list->init = NULL;
		list->size--;
	} else {
		node *aux = list->init;
		list->init = list->init->prox;
		list->init->ant = NULL;
		list->size--;
		free(aux);
	}
}

void popIn(List *list, int num){
	if(isEmpty(list)){
		printf("Nao existe item para ser removido. \n");
	} else if(num == list->last->num){
		pop(list);
	} else if (num == list->init->num){
		popFirst(list);
	} else {
		node *auxI = list->init->prox;
		node *auxF = list->last->ant;

		while ( (num != auxI->num) && (num != auxF->num)
		&& (auxI->prox != NULL)){
			auxI = auxI->prox;
			auxF = auxF->ant;
		}

		node *aux;
		if (num == auxF->num) {
			aux = auxF;
		} else if (num == auxI->num) {
			aux = auxI;
		} else {
			printf("Item nao encontrado... \n");
			return;
		}

		aux->ant->prox =  aux->prox;
		aux->prox->ant =  aux->ant;
		list->size--;
		free(aux);
	}

}

void popIndex(List *list, int pos){
	node *aux = list->init;
	int i;
	while ((i < pos) && (aux != NULL)){
		aux = aux->prox;
		i++;
	}

	if(aux == NULL){
		printf("posicao invalida \n");
	} else if(aux == list->last){
		pop(list);
	} else if (aux == list->init){
		popFirst(list);
	} else {
		aux->ant->prox = aux->prox;
		aux->prox->ant = aux->ant;
		list->size--;
		free(aux);
	}
}

void popAll(List *list){
	node *aux;
	while (list->init != NULL){
		aux = list->init;
		list->init = list->init->prox;
		free(aux);
	}

	list->last = NULL;
	list->size = 0;
}

void showFirst(List *list){
	if(!isEmpty(list)) printf("Primeiro numero: %d \n", list->init->num);
	else printf("Lista vazia. \n");
}

void showLast(List *list){
	if(!isEmpty(list)) printf("Ultimo Numero: %d \n", list->last->num);
	else printf("Lista vazia. \n");
}

// begin 1- vai do init at� last; 0- vai de last ate init
void showAll(List *list, int begin){
	if (begin){
		node *aux = list->init;
		while(aux != NULL){
			printf("Numero: %d \n", aux->num);
			aux = aux->prox;
		}
	} else {
		node *aux = list->last;
		while(aux != NULL){
			printf("Numero: %d \n", aux->num);
			aux = aux->ant;
		}
	}

}

void menu(List *list){
	int se = -1;
	while (se != 0){
		options();
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
				if(isEmpty(list)) printf("Lista esta vazia! \n");
				else printf("Lista nao esta vazia! \n");
				clean();
				break;
			case 3:
				showAll(list, 1);
				clean();
				break;
			case 4:
				showAll(list, 0);
				clean();
				break;
			case 5:
				showFirst(list);
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
			case 8:
				popFirst(list);
				clean();
				break;
			case 9:
				pop(list);
				clean();
				break;
			case 10:
				printf("Digite o numero: ");
				scanf("%d", &num);
				popIn(list, num);
				clean();
				break;
			case 11:
				printf("Digite o numero: ");
				scanf("%d", &num);
				popIndex(list, num);
				clean();
				break;
			case 12:
				popAll(list);
				clean();
				break;
			case 13:
				printf("Digite o numero: ");
				scanf("%d", &num);
				pushFirst(list, num);
				clean();
				break;
			case 14:
				printf("Digite o numero: ");
				scanf("%d", &num);
				pushIn(list, num);
				clean();
				break;
			case 0:
				return;
				break;
			default:
				system("cls");
				printf("Comando invalido. Digite novamente \n");
				break;
		}

	}
}

void options(){
	printf("01. Inserir \n");
	printf("02. verificar se esta vazia \n");

	printf("03. Exibir lista I/F\n");
	printf("04. Exibir lista F/I \n");
	printf("05. Exibir o primeiro e o ultimo \n");
	printf("06. Pesquisar aluno por nome \n");

	printf("07. Tamanho \n");

	printf("08. Remover o primeiro \n");
	printf("09. Remover o ultimo \n");
	printf("10. Remover numero \n");
	printf("11. Remover indice \n");
	printf("12. Apagar lista \n");

	printf("13. Inserir no inicio \n");
	printf("14. Inserir ordenado \n");

	printf("00. Sair \n");
}

void clean(){
	system("pause");
	puts("\x1b[H\x1b[2J");
}
