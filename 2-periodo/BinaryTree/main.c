#include <stdio.h>
#include <stdlib.h>

typedef struct elem {
	int value;
	struct elem *left, *right;	
} Node;

Node *createList();
int isEmpty(Node *root);

void preOrder(Node *tree);
void postOrder(Node *tree);
void inOrder(Node *tree);

void insert(Node **root, int value);

void menu(Node *root);
void options();
void clean();

int main (){
	Node *root = createList();
	menu(root);
	
	return 0;
}

Node *createList(){
	Node *tree = NULL;
	return tree;
}

int isEmpty(Node *root){
	return root == NULL;
}

void preOrder(Node *tree){
	if(tree != NULL){
		printf("%d ", tree->value);
		preOrder(tree->left);
		preOrder(tree->right);
		printf("\n");
	}
}

void postOrder(Node *tree){
	if(tree != NULL){
		preOrder(tree->left);
		preOrder(tree->right);
		printf("%d ", tree->value);
		printf("\n");
	}
}

void inOrder(Node *tree){
	if(tree != NULL){
		preOrder(tree->left);
		printf("%d ", tree->value);
		preOrder(tree->right);
		printf("\n");
	}
}

void insert(Node **root, int value){
	if (*root == NULL){
		*root = (Node *) malloc(sizeof(Node));
		(*root)->value = value;
		(*root)->left = NULL;
		(*root)->right = NULL;	
	} else if(value < ((*root)->value))
		insert(&((*root)->left), value);
	else
		insert(&((*root)->right), value);
}

void menu(Node *root){
	int se = -1;
	while (se != 0){
		options();
		scanf("%d", &se);

		int num;
		switch(se){
			case 1:
				printf("Digite o numero: ");
				scanf("%d", &num);
				insert(&root, num);
				clean();
				break;
			case 2:
				if(isEmpty(root)) printf("Arvore esta vazia! \n");
				else printf("Arvore nao esta vazia! \n");
				clean();
				break;
			case 3:
				preOrder(root);
				clean();
				break;
			case 4:
				postOrder(root);
				clean();
				break;
			case 5:
				inOrder(root);
				clean();
				break;
			case 0: exit(1);
			default:
				system("cls");
				printf("Comando invalido. Digite novamente \n");
		}

	}
}

void options(){
	printf("01. Inserir \n");
	printf("02. Verificar se esta vazia \n");

	printf("03. Pre ordem \n");
	printf("04. Pos ordem \n");
	printf("05. Em ordem \n");
	
	printf("00. Sair \n");
}

void clean(){
	system("pause");
	puts("\x1b[H\x1b[2J");
}
