#include <stdio.h>
#include <stdlib.h>

typedef struct elem {
	int value;
	struct elem *left, *right;	
} Node;

Node *createTree();
Node *getNode(Node *tree, int value);
Node *getMax(Node *tree);
int isEmpty(Node *root);
int getSum(Node *tree);
int getChild(Node *node);
int height(Node *tree);
int contPrimo(Node *tree);
int isPrimo(int num);
void setValue(Node *tree, int value, int num);
void setFolhas(Node *tree, int num);

void preOrder(Node *tree);
void postOrder(Node *tree);
void inOrder(Node *tree);
void insert(Node **root, int value);
void remov(Node **root, int value);
void swap(Node *node1, Node *node2);

int options();
void menu(Node *root);
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

Node *getMax(Node *tree){
	return !isEmpty(tree->right)? getMax(tree->right) : tree;
}

int getSum(Node *tree){
	return !isEmpty(tree)? tree->value + getSum(tree->left) + getSum(tree->right) : 0;
}

void postImpar(Node *tree){
	if(!isEmpty(tree)){
		postImpar(tree->left);
		postImpar(tree->right);
		if(tree->value % 2 != 0) printf("%d \n", tree->value);
	}
}

void preOrder10(Node *tree){
	if(!isEmpty(tree)){
		if(tree->value % 10 == 0) printf("%d \n", tree->value);
		preOrder10(tree->left);
		preOrder10(tree->right);
	}
}

int height(Node *tree){
	if(!isEmpty(tree)){
		int left = height(tree->left);
		int right = height(tree->right);
		return left >= right? left + 1 : right + 1;
	} else return 0;
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
	else return ((node->left != NULL) ^ (node->right != NULL))? 1 : 2;
}

int contPrimo(Node *tree){
	if(!isEmpty(tree)) {
		int primo = (isPrimo(tree->value))? 1 : 0;
		return primo + contPrimo(tree->left) + contPrimo(tree->right);
	} else return 0;
}

int isPrimo(int num){
	int primo = 0;
	if((num == 2) || (num % 2 != 0)){
		primo = 1;
		for(int i = 3; i < num; i += 2){
			if(num % i == 0) {
				primo = 0;
				break;
			}
		}	
	}
	return primo;
}

void setFolhas(Node *tree, int num){
	if (!isEmpty(tree)){
		tree->value += num;
		setFolhas(tree->left, num);
		setFolhas(tree->right, num);
	}
}

void setValue(Node *tree, int value, int num){
	Node *node = getNode(tree, value);
	if(node != NULL) node->value = num;
}

void swap(Node *node1, Node *node2){
	int aux = node1->value;
	node1->value = node2->value;
	node2->value = aux->value;
}

void menu(Node *root){
	while(1) {
		clean();
		int num, num2;
		switch(options()){
			case 1:
				printf("Digite o numero: ");
				scanf("%d", &num);
				insert(&root, num);
				break;
			case 2: postOrder(root); break;
			case 3: 
				isEmpty(root)? printf("vazia! \n") : printf("Nao vazia! \n"); 
				break;
			case 4: printf("Maior: %d \n", getMax(root)->value); break;
			case 5: printf("Soma: %d \n", getSum(root)); break;
			case 6: postImpar(root); break;
			case 7: printf("Altura: %d \n", height(root)); break;
			case 8: preOrder10(root); break;
			case 9: printf("Primos: %d \n", contPrimo(root)); break;
			case 10: 
				printf("Digite o numero ha somar com as folhas: ");
				scanf("%d", &num);
				setFolhas(root, num);
				break;
			case 11: 
				printf("Digite X: ");
				scanf("%d", &num);
				printf("Digite Y: ");
				scanf("%d", &num2);
				setValue(root, num, num2);
				break;
			case 2: break;
			case 2: break;
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
	printf("Swap    12. \n");
	printf("remove  13. \n");
	printf("Sair    00. \n");
	
	int se = -1;
	scanf("%d", &se);
	return se;
}

void clean(){
	puts("\x1b[H\x1b[2J");
	system("cls");
}

