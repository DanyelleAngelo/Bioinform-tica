/*
*Instituto Federal de Brasília
*Aluna: Danyellle da Silva Oliveira Angelo
*
*	Trabalho 3 de bioninformática
*/
#include <stdio.h>
#include "LIB/globalAlignment.h"

int main(int argc, char *argv[] ){
	GAP = -2, MISMATCHES = -1, MATCHES = 1;
	if(argc < 2){
		printf("E necessario indicar um arquivo de leitura\n");
		return 0;
	}
	performsAlignment(argv[1]);
}