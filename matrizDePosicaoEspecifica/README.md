Instituto Federal de Brasília<br>
Aluna: Danyellle da Silva Oliveira Angelo

	Trabalho 3 de bioninformática

* A versão do python usada nesse trabalho é a 3.6

* Para executar o programa, no terminal digite:

		python3 main.py

*Ao executar o programa será solicitado um arquivo de entrada, esse arquivo deve conter em cada linha  uma sequência de um box qualquer e a  quantidade de ocorrências que ela ocorre nas amostras disponíveis, separados por "\t". 

*O programa exibirá na tela 3 matrizes, são elas:matriz de frequência de cada resíduo em cada posição do alinhamento múltiplo,  matriz com as frequências normalizadas (com base na frequência total de cada resíduo) e matriz com os scores normalizados para escala logarítmica na base 2.
Além dessas matrizes o programa irá gerar um arquivo que tem como prefixo o nome do arquivo de entrada e sufixo a string "scores" que contém os scores desse alinhamento para cada sequência.