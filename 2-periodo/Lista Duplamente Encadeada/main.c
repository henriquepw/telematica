#include <stdio.h>
#include <stdlib.h>

typedef struct elem{
	int num;
	struct elem *ant, *prox;
} node;

typedef struct list{
	int size;
	node *init;
	node *last;
} List;

List *createList();
node *alloc(int num);
int isEmpty(List *list);

void push(List *list, int num);
void pushFirst(List *list, int num);
void pushIn(List *list, int num);

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
  return list->size == 0;
}

void push(List *list, int num){
	node *novo = alloc(num);

	if(isEmpty(list)){
		list->init = novo;
		list->last = novo;
	} else {
		list->last->prox = novo;
		novo->ant = list->last;
		list->last = novo;
	}
	
	list->size++;

}

void pushFirst(List *list, int num){
	node *novo = alloc(num);

	if(isEmpty(list)){
		list->init = novo;
		list->last = novo;
		list->size++;
	} else {
		novo->prox = list->init;
		list->init->ant = novo;
		list->init = novo;
		list->size++;
	}
}

void pushIn(List *list, int num){
  
  if (isEmpty(list)){
  	node *novo = alloc(num);
    list->init = novo;
    list->last = novo;
    
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
	if(num > auxL->num)
		aux = auxL;
	else
		aux = auxI;
		
	node *novo = alloc(num);
	novo->prox = aux->prox;
	novo->ant = aux;
	aux->prox = novo;
	  
  }
}

void showFirst(List *list){
	if(!isEmpty(list))
		printf("Primeiro numero: %d \n", list->init->num);
	else
		printf("Lista vazia. \n");
}

void showLast(List *list){
	if(!isEmpty(list))
		printf("Ultimo Numero: %d \n", list->last->num);
	else
		printf("Lista vazia. \n");
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
		printf("12. Inserir na frente de {Nome do aluno} \n");
		
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
