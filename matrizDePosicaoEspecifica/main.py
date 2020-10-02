"""
    Instituto Federal de Brasília.
    Aluna: Danyelle da Silva Oliveira Angelo.
"""

import writingReading as wr
import frequencyMatrix as fm

def main():
    filename = input("Arquivo de entrada (.motif): ")
    if filename:
    	sequences, totalSequences = wr.readFile(filename)
    if sequences:
        frequencyMax = fm.fn_frequencyMatrix(sequences,totalSequences)
        wr.imprimir(frequencyMax,"Matriz de frequência de cada resíduo")
        frequencyMax = fm.normalizedMatrixOverralFrequency(frequencyMax)
        wr.imprimir(frequencyMax,"Matriz normalizada através da frequência geral")
        frequencyMax = fm.matrixNormalizedScore(frequencyMax)
        wr.imprimir(frequencyMax,"Matriz com os scores normalizados para escala logarítmica na base 2")
        scoreSequences = fm.calculateScore(sequences,frequencyMax)
        wr.writeScoreTabularFile(scoreSequences,filename)

if __name__ == "__main__":
    main()