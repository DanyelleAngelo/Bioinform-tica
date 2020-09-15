Instituto Federal de Brasília
Aluna: Danyellle da Silva Oliveira Angelo

	Trabalho 3 de bioninformática


* Para executar o programa, no terminal digite:
	./pairwiseglobal arquivo.fasta

	- O arquivo fasta <b>deverá obrigatoriamente conter 2 sequências, iniciadas com o símbolo ">" e com no máximo 100 caracteres cada</b>, para
	sequências maiores recomenda-se a implementação desse programa usando listas.
	
	-Deixei aqui um arquivo fasta de exemplo(input.fasta).

	<b>Obs.: Não se esqueça de fornecer o arquivo fasta como argumento para o programa</b>

* Caso seja necessário recompilar o programa principa ou alguma função usada por ele faça o seguinte:
	- No terminal digite os comandos:
		gcc -c LIB/globalAlignment.c
		ar rcs LIB/globalAlignment.a LIB/globalAlignment.o
		gcc pairwiseglobal.c -o pairwiseglobal LIB/globalAlignment.a
	- Agora é só executar conforme mostrado no ínicio.