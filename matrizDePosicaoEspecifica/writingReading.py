"""
	Instituto Federal de Brasília.
	Aluna: Danyelle da Silva Oliveira Angelo.
	

	Contém as funções de leitura e escrita em arquivos, além da função de impressão das matrizes de frequências.
"""


def readFile(filename):
    """
        Lê linha por lnha do arquivo e  armazena cda linha do arquivo em um dicionário
        (dividindo o conteudo em: sequência e ocorrencia) e armazena estes dicionários em
        uma lista que e retornada pela função.
    """
    sequences = []
    totalSequences = 0
    try:
    	with open(filename, 'r') as fp:
	        i = 0
	        for line in fp:
	            line = line.replace("\n","")
	            line = line.split("\t")
	            try:
	                sequence = line[0]
	                occurrences = int(line[1])
	                sequences.append({"seq":sequence,"occurrences":occurrences})
	                totalSequences += occurrences
	                i+=1
	            except ValueError:
	                print("Ocorreu um erro na leitura da sequência %s" %(sequence))
    except FileNotFoundError:
    	print("Ocorreu um erro ao tentar abrir o arquivo %s" %filename)
    return sequences,totalSequences

def imprimir(matrix,msgm):
	"""
		Imprime as matrizes geradas acompanhadas do seu rótulo
	"""
	hr = "-"*25
	print("\n\t %s %s %s \n"%(hr,msgm,hr))
	for key,values in matrix.items():
		if key!= "header":
			print(key,end="\t\t")
		for obj in values:
			if(type(obj)  == float):obj = format(obj,".4f")
			print("%s" %obj,end="\t\t")
		print()
	print("\n\n")


def writeScoreTabularFile(scoreSequences,filename):
	"""
		Grava em um arquivo filename.scores as amostras de dterminado organismo e seu respectivo socre.
		Esses dados são gravados de forma tabular, separados por ";""
	"""
	filename = "%s.scores" %filename
	with open(filename,"w") as fp:
		fp.write("Sequence; Score;\n")
		for sequence in scoreSequences:
			for key in sequence:
				if(key!="occurrences"):
					fp.write("%s;" %sequence[key])
			fp.write("\n")