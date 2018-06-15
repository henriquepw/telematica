#include <stdio.h>
#include <stdlib.h>

typedef struct elem{
	int matricula;
	float media;
	struct elem *ant, *prox; 
} node;

typedef struct ele{
	int matricula;
	float media;
	struct ele *prox;	
} node2;

typedef struct list{
	int size;
	node *INI, *FIM;
} List;

void menu(List *);
void clean();

// Questao 1
List *iniciar();
int isEmpty(List *);
node *alloc(float, int);
void insere(List *, float, int);

// Questao 2
node2 *pilha(node2 *, int, float);
node2 *fila(node2 *, int, float);
node2 *converte(List *, int);
void exibeLSE(node2 *);

// Questao 3
void exibe(List *, int);
void printAluno(node *);

List *iniciar(){
	List *list = (List *)malloc(sizeof(List));
	list->INI = NULL;
	list->FIM = NULL;
	list->size = 0;
}

int isEmpty(List *list){
	return ((list->INI == NULL) && (list->FIM == NULL));
}

void insere(List *list, float media, int matricula){
	node *novo = alloc(media, matricula);
	if(isEmpty(list)){
		list->INI = novo;
		list->FIM = novo;
	} else if(media > list->FIM->media){
		list->FIM->prox = novo;
		novo->ant = list->FIM;
		list->FIM = novo;
	} else if(media < list->INI->media){
		list->INI->ant = novo;
		novo->prox = list->INI;
		list->INI = novo;
	} else {
		node *aINI = list->INI;
		node *aFIM = list->FIM;
		
		while ((media > aINI->media) && (media < aFIM->media)){
			aINI = aINI->prox;
			aFIM = aFIM->ant;
		}
		
		node *aux;
		if(media > aFIM->media) aux = aFIM;
		else aux = aINI->ant;
		
		novo->prox = aux->prox;
		novo->ant = aux;
		aux->prox->ant = novo;
		aux->prox = novo;
	}
	list->size++;
}

/*Questao 02*/
node2 *pilha(node2 *list, int matricula, float media){
  printf("Entrou na pilha \n");
  node2 *novo = (node2 *)malloc(sizeof(node2));
  novo->matricula = matricula;
  novo->media = media;
  novo->prox = NULL;
  
  if(list == NULL){
    list = novo;
  } else {
    list->prox = novo; 
    list = novo;
  }
  
  return list;
}

node2 *fila(node2 *list, int matricula, float media){
  printf("Entrou na fila \n");
  node2 *novo = (node2 *)malloc(sizeof(node2));
  novo->matricula = matricula;
  novo->media = media;
  novo->prox = NULL;

  if(list == NULL){
    list = novo;
  } else {
    node2 *aux = list;
    while (aux->prox != NULL){
      aux = aux->prox;
    }
    aux->prox = novo;
  }
  
  return list;
}

node2 *converte(List *list, int begin){
  node2 *lista = NULL;

  if(!isEmpty(list)){
    if(begin > 0){
      printf("Tem que exibir os impares \n");
      if(list->size > 2){
      	printf("Maior que dois \n");
        node *aux = list->INI->prox;
        
        for(int i = 1; i <= list->size-1; i++){
        	if(i % 2 != 0){
	          lista = fila(lista, aux->matricula, aux->media);
	    	}
	    	aux = aux->prox;
		}

      } else if(list->size == 2){
      	printf("Menor que dois \n");		
        lista = fila(lista, list->INI->prox->matricula, list->INI->prox->media);
      }

    } else if (begin < 0){
    	printf("Tem que exibir os pares \n");
        if(list->size > 2){
          printf("Maior que dois \n");
          node *aux = list->INI;

          for(int i = 0; i <= list->size-1; i++){
          	if(i % 2 == 0)
          		lista = pilha(lista, aux->matricula, aux->media);

			aux = aux->prox;
		  }

        } else {
          printf("Menor que dois \n"); 
          lista = pilha(lista, list->INI->matricula, list->INI->media);
        }
    }
  }
  
  return lista;
}

/*Fim questão 02*/

void exibeLSE(node2 *lista){
	node2 *aux = lista;
	while(aux != NULL){
		printf(" - Matricula: %d \n", aux->matricula);
		printf(" - Media: %2.f \n", aux->media);
		printf(" ----- \n");
		aux = aux->prox;
	}
}

node *alloc(float media, int matricula){
	node *novo = malloc(sizeof(node));
	novo->matricula = matricula;
	novo->media = media;
	novo->prox = NULL;
	novo->ant = NULL;
	
	return novo;
}

void exibe(List *list, int begin){
	node *aux;
	if(begin > 0){
		aux = list->INI;
		while (aux != NULL){
			printAluno(aux);
			aux = aux->prox;
		}
	}else if(begin < 0){
		aux = list->FIM;
		while (aux != NULL){
			printAluno(aux);
			aux = aux->ant;
		}
	}else {
		aux = list->INI;
		while (aux != NULL){
			if(aux->media >= 7.0)
				printAluno(aux);
			aux = aux->prox;
		}
	}
}

void printAluno(node *aluno){
	printf(" - Matricula: %d \n", aluno->matricula);
	printf(" - Media: %2.f \n", aluno->media);
}

void menu(List *list){
	int se = -1;
	node2 *lista = (node2 *)NULL;
	
	insere(list, 0, 0);
	insere(list, 1, 1);
	insere(list, 2, 2);
	
	
	while (se != 0){
		printf("1. Insere \n");
		printf("2. exibe inicio a fim \n");
		printf("3. exibe fim a inicio \n");
		printf("4. exibe acima da media \n");
		printf("5. converte LSE inpares \n");
		printf("6. converte LSE pares \n");
		printf("7. Tamanho da LDE \n");
		printf("0. sair \n");
		
		float media;
		int matricula;
		scanf("%d", &se);
		clean();
		switch(se){
			case 1: 
				scanf("%d", &matricula);
				scanf("%f", &media);
				insere(list, media, matricula);
				break;
			case 2: exibe(list, 1); break;
			case 3: exibe(list, -1); break;
			case 4: exibe(list, 0); break;
			case 5:
				lista = converte(list, 1);
				exibeLSE(lista);
				break;
			case 6:
				lista = converte(list, -1);
				exibeLSE(lista);
				break;
			case 7:
				printf("%d \n", list->size);
		}
	}
}

int main(){
	List *alunos = iniciar();
	menu(alunos);
	
	return 0;	
}

void clean(){
	system("cls");
	puts("\x1b[H\x1b[2J");
}

