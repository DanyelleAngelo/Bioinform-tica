import re

def readingsBoards(sequences,complementary):
	"""
		Identifica os quadros de leitura de  n sequências e os imprime no arquivo definido pela variável filename
	"""
	filename = "orfs.fasta"

	with open(filename,"w") as fp:
		for i in range(len(sequences)):
			size = len(sequences[i])
			#imprime os boards da fita original
			end = size
			for board in range(3):
				fp.write(">orf +%d \n" %(board+1))
				fp.write(sequences[i][board:end])
				fp.write("\n")
				end = end - 2

			#imprime os boards da fita complementar
			end = size
			for board in range(3):
				fp.write(">orf -%d \n" %(board+1))
				fp.write(complementary[i][board:end])
				fp.write("\n")
				end = end - 2

def complementaryTape(sequences):
	"""
		Cria a fita complementar de n sequências.

	"""
	complementary = []
	bases= {"a":"T","t":"A","c":"G","g":"C"}
	for seq in sequences:
		temp = seq[::-1].lower() #a fita e geradano sentid 3'->5'. marcamos os nucleotídeos não trocados através da representação  em letra minscúla
		for key, values in bases.items():
			temp = re.sub(key,values,temp)#faz a correspodência de bases
		complementary.append(temp)
	return complementary


def readFile(filename):
	"""
		Retornan  sequências
	"""
	sequences = []
	seq = re.compile(">")#caso venha expandir os cabeçalhos
	try:
		with open(filename, 'r') as fp:
			for line in fp:
				if seq.search(line) is None:
					sequences.append(line)
	except FileNotFoundError:
		print("Ocorreu um erro ao tentar abrir o arquivo %s" %filename)
	return sequences

def main():
	sequences = []
	complementary = []
	filename = "gene.fasta"
	if filename:
		sequences = readFile(filename)
		complementary = complementaryTape(sequences)
		if complementary:
			readingsBoards(sequences,complementary)
		else:
			print("Ocorreu um erro ao tentar gerar as sequências complementares!")

if __name__ == "__main__":
	main()