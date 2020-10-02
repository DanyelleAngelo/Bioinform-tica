import math

def matrixNormalizedScore(matrix):
	"""
		Normaliza a matriz de frequências, dividindo cada frequência por log na base 2
	"""
	matrixNormalized = matrix.copy()
	lines = len(matrix)
	cols = len(matrix[0])
	for line in range(lines):
		if line !=0:
			for col in range(cols):
				if col!=0 and float(matrix[line][col])>0:
					matrixNormalized[line][col] = format(math.log(float(matrix[line][col]), 2.0),'.4f')

	return matrixNormalized

def createMatrix(frequencys,totalSequences,totalN):
    """
        Cria a matriz com a frequência de cada nucleotideo.
    """
    matrix = []
    qtdNucleotides = len(frequencys)
    header = [x+1 for x in range(qtdNucleotides)]
    header.insert(0,"Pos.")
    header.insert(qtdNucleotides+1,"Overral freq.")
    matrix.append(header)
    
    for nucleotide, occurrences in frequencys.items():
        line = [0]* (qtdNucleotides+2)
        line[0] = nucleotide
        total = 0
        for column, i in occurrences.items():
            line[column] = format(i/totalSequences,'.4f')
            total += i 
        line[qtdNucleotides+1] = format(total/totalN,'.4f')
        matrix.append(line)
        
    return matrix

def calculateFrequency(sequences,totalSequences):
    """
        Cria um dict com a quantidade de ocorrências de um nucleotideo para cada coluna.
    """
    frequencys = {}
    for seq in sequences:
        i = 1
        for c in seq["seq"]:
            if c not in frequencys:
                #esse nucleotideo ainda nao foi encontrado em nenhuma sequência
                frequencys[c]= {i:seq["ocurrences"]}
            else:
                #esse nucletideo ja foi lido em outra sequência
                #esse nucleotieo ja foi em outra sequência na coluna i
                if i in frequencys[c]:
                    frequencys[c][i] += seq["ocurrences"]
                else:
                    #esse nucleotideo nao foi lido na posicao i
                    frequencys[c][i] = seq["ocurrences"]
            i+=1  
    return frequencys
    
def frequencyMatrix(sequences,totalSequences):
    '''
        Recebe como parâmetro uma lista com as sequências e o total de vezes que estas aparecem,
        e cria uma matriz com as frequências de cada nucleotideo.
    '''
    matrix = []
    frequencys =  calculateFrequency(sequences,totalSequences)
    totalN = len(frequencys) * totalSequences
    matrix = createMatrix(frequencys,totalSequences,totalN)
    
    return matrix

def readFile():
    """
        Lê linha por lnha do arquivo e  armazena cda linha do arquivo em um dicionário
        (dividindo o conteudo em: sequência e ocorrencia) e armazena estes dicionários em
        uma lista que e retornada pela função.
    """
    filename = "D.motif"
    sequences = [] 
    totalSequences = 0
    with open(filename, 'r') as fp:
        i = 0
        for line in fp:
            line = line.replace("\n","")
            line = line.split("\t")
            try:
                sequence = line[0]
                occurrences = int(line[1])
                sequences.append({"seq":sequence,"ocurrences":occurrences})
                totalSequences += occurrences
                i+=1
            except ValueError:
                print("Ocorreu um erro na leitura da sequência %s" %(sequence))
        
    return sequences,totalSequences

def imprimir(matrix,msgm):
	print(msgm)
	for line in matrix:
		print(line)

def writeTabularFile():
	pass

def main():
    sequences, totalSequences = readFile()
    if sequences:
        frequencyMax = frequencyMatrix(sequences,totalSequences)
        imprimir(frequencyMax,"\n\t\tMatriz de frequência")
        #dividir pela frequencia geral
        matrix = matrixNormalizedScore(frequencyMax)
        imprimir(matrix,"\n\tMatriz com os scores normalizados para escala logarítmica na base 2")
        #calcular o score de cada sequencia
if __name__ == "__main__":
    main()