#include <stdio.h>
#include <stdlib.h>

typedef struct elem{
	int salario;
	int matricula;
	struct elem *esq, *dir;	
} Node;

Node *createTree();
int isEmpty(Node *);
void preOrder(Node *);

void menu(Node *root);
int questoes();

//questao 1
void insert(Node **tree, int matricula, int salario);

//questao 2
int vice(Node *tree);

//questao 3
int somaChefe(Node *tree);

int main (){
	Node *root = createTree();
	menu(root);
	return 0;
}

Node *createTree(){
	Node *tree = NULL;
	return tree;
}

int isEmpty(Node *node){
	return node == NULL;
}

void preOrder(Node *node){
	if(!isEmpty(node)){
		printf("Matricula %d: R$ %d \n", node->matricula, node->salario);
		preOrder(node->esq);
		preOrder(node->dir);
	}
}

void insert(Node **tree, int matricula, int salario){
	if(isEmpty(*tree)){
		*tree = (Node *) malloc(sizeof(Node));
		(*tree)->matricula = matricula;
		(*tree)->salario = salario;
		(*tree)->esq = NULL;
		(*tree)->dir = NULL;

	} else if(salario > (*tree)->salario) {
		insert(&((*tree)->dir), matricula, salario);
	} else {
		insert(&((*tree)->esq), matricula, salario);
	}	
}

int tamanhoDir(Node *node){
	return (!isEmpty(node))? 1 + tamanhoDir(node->dir) : 0;
}

int vice(Node *tree){
	if (!isEmpty(tree)){
		if(tamanhoDir(tree) >= 2)
			return (!isEmpty(tree->dir->dir))? vice(tree->dir) : tree->matricula;
		else
			return (!isEmpty(tree->esq))? (tree->esq)->matricula : 0;	
	} else return 0;
}

int max(Node *tree){
	return (!isEmpty(tree->dir))? max(tree->dir) : tree->matricula;
}

int somaChefe(Node *tree){
	if(!isEmpty(tree)){
		int soma = 0;
		if((tree->esq != NULL) || (tree->dir != NULL)) 
			soma =  tree->salario;
		
		soma += somaChefe(tree->esq) + somaChefe(tree->dir);
		return soma;
	} return 0;
}

void menu(Node *root){
	while(1){
		int matricula, salario;
		system("cls || clear");
		switch(questoes()){
			case 1:
				do {
					printf("Matricula (se 0, para de inserir): \n");
					scanf("%d", &matricula);
					
					if(matricula != 0){
						printf("Salario: \n");
						scanf("%d", &salario);
						insert(&root, matricula, salario);
					}
				} while (matricula != 0);
				break;
			case 2: printf("Vice: %d \n", vice(root)); break;
			case 3: printf("SomaChefe: %d \n", somaChefe(root)); break;
			case 4: preOrder(root); break;
			case 0: exit(1);
		}
		system("pause");
	}
}

int questoes(){
	printf("Questao   1 \n");
	printf("Questao   2 \n");
	printf("Questao   3 \n");
	printf("preOrder  4 \n");
	printf("Sair      0 \n");
	
	int se;
	scanf("%d", &se);
	return se;
}


