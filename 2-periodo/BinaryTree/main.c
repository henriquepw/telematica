#include <stdio.h>
#include <stdlib.h>

typedef struct elem {
	int value;
	struct elem *left, *right;	
} Node;

int isEmpty(Node *root);
Node *createTree();
Node *getNode(Node *tree, int value);
int getChild(Node *node);

void preOrder(Node *tree);
void postOrder(Node *tree);
void inOrder(Node *tree);

void insert(Node **root, int value);
void remov(Node **root, int value);
void swap(Node **root, int value1, int value2);

Node *max(Node *tree);
Node *sum(Node *tree);

void menu(Node *root);
int options();
void clean();

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

void preOrder(Node *tree){
	if(!isEmpty(tree)){
		printf("%d \n", tree->value);
		preOrder(tree->left);
		preOrder(tree->right);
	}
}

void postOrder(Node *tree){
	if(!isEmpty(tree)){
		preOrder(tree->left);
		preOrder(tree->right);
		printf("%d \n", tree->value);
	}
}

void inOrder(Node *tree){
	if(!isEmpty(tree)){
		preOrder(tree->left);
		printf("%d \n", tree->value);
		preOrder(tree->right);
	}
}

void insert(Node **root, int value){	
	if (isEmpty(*root)){
		*root = (Node *) malloc(sizeof(Node));
		(*root)->value = value;
		(*root)->left = NULL;
		(*root)->right = NULL;
	} else if(value < ((*root)->value))
		insert(&((*root)->left), value);
		
	else if(value > ((*root)->value))
		insert(&((*root)->right), value); 
}

Node *max(Node *tree){
	return !isEmpty(tree->right)? max(tree->right) : tree;
}

Node *sum(Node *tree){
	
}

void remov(Node **root, int value){
	if(isEmpty(*root)) printf("Arvore vazia \n");	
	else switch(getChild(*root)){
			case 1:
				 
				break;
			case 2:
				 
				break;
			case 3:
				 
				break;
		}
}

Node *getNode(Node *tree, int value){
	if(isEmpty(tree)) return NULL;
	else if(tree->value == value) return tree;
	else if (tree->value > value) getNode(tree->left, value);
	else if (tree->value < value) getNode(tree->right, value);
}

int getChild(Node *node){
	if((node->left == NULL) && (node->right == NULL)) return 0;
	else if((node->left != NULL) || (node->right != NULL)) return 1;
	else return 2;
}

void menu(Node *root){
	while(1) {
		clean();
		int num;
		switch(options()){
			case 1:
				printf("Digite o numero: ");
				scanf("%d", &num);
				insert(&root, num);
				break;
			case 2: postOrder(root); break;
			case 3:
				(isEmpty(root))? printf("Arvore esta vazia! \n") : printf("Arvore nao esta vazia! \n");
				break;
			case 4: printf("Maior: %d \n", max(root)->value); break;
			case 5: break;
			case 6: break;
			case 7: break;
			case 8: break;
			case 9: break;
			case 10: break;
			case 0: exit(1);
			default: printf("Comando invalido. ");
		}
		system("pause");
	}
}

int options(){
	printf("Questao 01. \n");
	printf("Questao 02. \n");
	printf("Questao 03. \n");
	printf("Questao 04. \n");
	printf("Questao 05. \n");
	printf("Questao 06. \n");
	printf("Questao 07. \n");
	printf("Questao 08. \n");
	printf("Questao 09. \n");
	printf("Questao 10. \n");
	printf("Questao 11. \n");
	printf("Sair    00. \n");
	
	int se = -1;
	scanf("%d", &se);
	return se;
}

void clean(){
	puts("\x1b[H\x1b[2J");
	system("cls");
}

