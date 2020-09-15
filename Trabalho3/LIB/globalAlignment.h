/*
*Instituto Federal de Brasília
*Aluna: Danyellle da Silva Oliveira Angelo
*
*	Trabalho 3 de bioninformática
*/
#ifndef GLOBALALIGN_H
#define GLOBALALIGN_H

/*CONSTANTES DE PONTUAÇÕES*/
int GAP, MISMATCHES, MATCHES, MAX_SCORE;

/*
*@brief realiza a leitura de 2 linhas do arquivo, abortando o programa caso seja impossível abrir o arquivo
*@param sq1: vetor de caracteres correspondente a sequência 1
*@param sq2: vetor de caracteres correspondente a sequência 2
*/
void readFile(char *filename, char *sq1, char *sq2);

/*
*@brief retornar maior elemento
*@param a,b,c: inteiros
*@return: a ou b ou c
*/
int max(int a,int b,int v);

/*
*@brief aloca uma matriz de inteiro linesXcols posições
*@param lines: número de linhas da matriz
*@param cols: número de colunas da matriz
*@return: matriz de inteiros
*/
int **alocaMatrix(int lines, int cols);

/*
*@brief libera espaço usadoo por uma matriz de inteiros
*@param mat: matriz de inteiros
*@param lines: quantidade de linhas na matriz
*/
void freeMatrix(int **mat,int lines);

/*
*@brief recebe o endereço de um arquivo e chama as funções responsáveis pela leitura e pelo alinhamento da sequência
*@param filename: caminho/name_archive.fasta
*/
void performsAlignment(char *filename);

/*
*@brief solicita a leitura de um arquivo para a captura das sequencias analisadas,e o preenchimento da matriz de pontuação.
*@param mat: matriz de pontuação
*@param lines: número de linhas da matriz (= tamanho de sq1)
*@param cols: número de colunas da matriz (= tamanho de sq2)
*@param sq1: vetor de caracteres correspondente a sequência 1
*@param sq2: vetor de caracteres correspondente a sequência 2
*/
void fillsMatrix(int **mat,int lines,int cols,char *sq1,char *sq2);

/*
*@brief realiza a impressão da matriz de pontuação
*@param mat: matriz de pontuação
*@param sq1: vetor de caracteres correspondente a sequência 1
*@param sq2: vetor de caracteres correspondente a sequência 2
*/
void print(int ** mat, char *sq1, char *sq2);

/*
*@brief cria 2 vetores com o melhor alinhamento possível  e os envia para inertSequence
*@param mat: matriz de pontuação
*@param sq1: vetor de caracteres correspondente a sequência 1
*@param sq2: vetor de caracteres correspondente a sequência 2
*@param lines: número de linhas da matriz (= tamanho de sq1)
*@param cols: número de colunas da matriz (= tamanho de sq2)
*/
void bestSequence(int **mat, char *sq1,char *sq2,int lines,int cols);

/*
*@brief inverte 2 sequências para o sentido 5'-3' e imprime as mesmas
*@param sq1: vetor de caracteres correspondente a sequência 1
*@param sq2: vetor de caracteres correspondente a sequência 2
*/
void invertSequence(char *sq1,char *sq2);

#endif