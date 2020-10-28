"""
    Instituto Federal de Brasília.
    Aluna: Danyelle da Silva Oliveira Angelo.

    Este arquivo contém as funções de montagem e cáclulo das matrizes de frequência.
"""
import math
from collections import OrderedDict 


def fn_frequencyMatrix(sequences,totalSequences):
    '''
        Recebe como parâmetro uma lista com as sequências e o total de vezes que estas aparecem,
        e cria uma matriz com as frequências de cada nucleotideo.
    '''
    matrix = []
    frequencys =  calculateFrequency(sequences,totalSequences)
    totalNucl = len(frequencys) * totalSequences
    nuclQttLine = len(sequences[0]["seq"])
    matrix = createMatrix(frequencys,totalSequences,totalNucl,nuclQttLine)
    
    return matrix

def calculateFrequency(sequences,totalSequences):
    """
        Cria um dict com a quantidade de ocorrências de um nucleotideo para cada coluna.
    """
    frequencys = {}
    for seq in sequences:
        i = 0
        for nucl in seq["seq"]:
            if nucl not in frequencys:
                #esse nucleotideo ainda nao foi encontrado em nenhuma sequência
                frequencys[nucl]= {i:seq["occurrences"]}
            else:
                #esse nucletideo ja foi lido em outra sequência
                #esse nucleotieo ja foi em outra sequência na coluna i
                if i in frequencys[nucl]:
                    frequencys[nucl][i] += seq["occurrences"]
                else:
                    #esse nucleotideo nao foi lido na posicao i
                    frequencys[nucl][i] = seq["occurrences"]
            i+=1  
    return frequencys

def createMatrix(frequencys,totalSequences,totalNucl,nuclQttLine):
    """
        Cria a matriz com a frequência de cada nucleotideo.
    """
    matrix = OrderedDict()
    header = [x+1 for x in range(nuclQttLine)]
    header.insert(0,"Pos.")
    header.insert(nuclQttLine+1,"Overral freq.")
    matrix["header"] = header
    for nucleotide, columns in frequencys.items():
        line = [0]* (nuclQttLine+1)
        total = 0
        for column, qtt in columns.items():
            line[column] = qtt/totalSequences
            total += qtt
        line[nuclQttLine] = total/totalNucl
        
        matrix[nucleotide] = line
        
    return matrix

def normalizedMatrixOverralFrequency(matrix):
    """
        Normaliza a matrix dividindo a frequência de cada nucletídeo pela sua frequência geral.
    """
    cols = len(matrix["header"]) -1
    for line in matrix:
        if line != "header":
            overralFrequency = float(matrix[line][cols-1])
            for col in range(cols-1): 
                matrix[line][col]  =  float(matrix[line][col])/overralFrequency

    return matrix

def matrixNormalizedScore(matrix):
	"""
		Normaliza a matriz de frequências, dividindo cada frequência por log na base 2
	"""
	cols = len(matrix["header"]) -1
	for line in matrix:
		if line != "header":
			for col in range(cols-1): 
				if float(matrix[line][col])>0:
					matrix[line][col] = math.log(float(matrix[line][col]), 2.0)

	return matrix
    
def calculateScore(sequences,frequencyMax):
	scoreSequences = sequences.copy()
	for sequence in sequences:
		i = 0
		score = 0
		for nucl in sequence["seq"]:
			score += float(frequencyMax[nucl][i])
			i+=1
		sequence["score"] = format(score,".4f")

	return scoreSequences