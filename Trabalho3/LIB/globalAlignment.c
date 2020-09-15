/*
*Instituto Federal de Brasília
*Aluna: Danyellle da Silva Oliveira Angelo
*
*	Trabalho 3 de bioninformática
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "globalAlignment.h"

void readFile(char *filename, char *sq1, char *sq2){
	FILE *fp;

	fp = fopen(filename,"r");
	if(fp == NULL){
		printf("Ocorreu um erro no momento de leitura dos dados!\n");
		exit(1);
	}
	fscanf(fp,"%s",sq1); //fgets(line, 100, fp);
	fscanf(fp,"%s",sq2);//fgets(line, 100, fp);
	fclose(fp);
}

int max(int a,int b,int c){
	if(a > b && a >= c){
		return a;
	}
	if(c >= a && c > b){
		return c;
	}
	if(b >= a && b >= c){
		return b;
	}
}

int **alocaMatrix(int lines, int cols){
	int **mat,i;
	mat = (int**)malloc(lines * sizeof (int*));
	if(mat == NULL){
		printf("Ocorreu um erro ao montar a matrix de dados!\n");
		exit(1);	
	}
	for(i=0;i<lines;i++){
		mat[i] = (int*)malloc(cols * sizeof (int));
	}
	return mat;
}

void freeMatrix(int **mat,int lines){
	int i;
	for(i=0; i < lines; i++)free (mat[i]);
	free(mat);
}

void performsAlignment(char *filename){
	char sq1[100],sq2[100];
	int **mat,lines,cols;
	
	readFile(filename,sq1,sq2);

	lines = strlen(sq1);
	cols = strlen(sq2);
	mat = alocaMatrix(lines,cols);

	fillsMatrix(mat,lines,cols,sq1,sq2);
	print(mat, sq1,sq2);
	printf("\n");

	printf("O score maximo e %d\n",MAX_SCORE);
	printf("\n");

	bestSequence(mat,sq1,sq2,lines,cols);

	freeMatrix(mat,lines);
}

void fillsMatrix(int **mat,int lines,int cols,char *sq1,char *sq2){
	int i,j,aV,aD,aH;

	for(i=0;i<cols;i++){
		//preenchendo linha 0,ela é fixa
		mat[0][i] = i*(-2);
	}
	for(j=0;j<lines;j++){
		//preenchendo a coluna 0,linhas variaveis
		mat[j][0] = j*(-2);

	}

	for(i=1;i<lines;i++){
		for(j=1;j<cols;j++){
			aV = mat[i-1][j] + GAP;//anterior vertical
			aH = mat[i][j-1] + GAP;//anterior horziontal
			aD = (sq1[i] == sq2[j]) ? mat[i-1][j-1] + MATCHES: mat[i-1][j-1] + MISMATCHES;//anterior diagonal
			mat[i][j] = max(aV,aD,aH);
		}
	}

	MAX_SCORE = mat[lines-1][cols-1];
}

void print(int ** mat, char *sq1, char *sq2){
	int i,j;
	printf("\tMatriz de pontuacao\n");
	for(j=0;j<strlen(sq2);j++){
		if(j==0)printf("\t");
		printf("%c\t",sq2[j]);
	}
	printf("\n");

	for(i=0;i<strlen(sq1);i++){
		printf("%c\t",sq1[i]);
		for(j=0;j<strlen(sq2);j++){
			printf("%d \t", mat[i][j]);
		}
		printf("\n");
	}
}

void bestSequence(int **mat, char *sq1,char *sq2,int lines,int cols){
	int i, j=cols-1,k=0,m=0;
	char seq1[200],seq2[200]; 
	printf("O melhor alinhamento e:\n");
	for(i=lines-1;i>0;){
		if(mat[i][j] == mat[i-1][j-1] + MATCHES || mat[i][j] ==  mat[i-1][j-1]+MISMATCHES){
			//alinha nucleotideo com nucleotideo
			seq1[k] = sq1[i];
			seq2[m] = sq2[j];
			i--;
			j--;
		}
		else if(mat[i][j] == (mat[i-1][j] + GAP)){
			//gap na sequencia horizontal
			seq1[k] = sq1[i];
			seq2[m] ='-';
			i--;
		}else if(mat[i][j] == (mat[i][j-1] + GAP)){
			//gap na sequencia vertical
			seq1[k] = '-';
			seq2[m] = sq2[j];
			j--;
		}
		k++;
		m++;
	}
	seq1[k] = '\0';
	seq2[m] = '\0';
	invertSequence(seq1,seq2);
	printf("%s\n%s\n",seq1,seq2);
}

void invertSequence(char *sq1,char *sq2){
	int i,j,n = strlen(sq1);
	char sq1Temp[n],sq2Temp[n];
	strcpy(sq1Temp,sq1);
	strcpy(sq2Temp,sq2);
	for(j=0, i=n-1;i>-1;i--,j++){
		sq1[j]=sq1Temp[i];
		sq2[j]=sq2Temp[i];
	}
}

