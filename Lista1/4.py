'''
Instituto Federal de Brasília - Campus: Taguatinga
Aluna: Danyelle da Silva Oliveira Angelo.
Professor: João Victor de Oliveira Araújo - Disciplina: Bioinformática - 2020
'''
def readFile():
	filename = "sequence.fasta"
	list_sequence = []
	with open(filename, 'r') as fp:
		for header,sequence in  zip(fp,fp):
			header = header.replace(">","").replace("\n","")
			sequence = sequence.replace("\n","")
			list_sequence.append((header,sequence))
	return list_sequence

def printListSequence(list_sequence):
	for header,sequence in list_sequence:
		print("(%s,%s)" %(header,sequence))

def main():
	list_sequence = readFile()
	printListSequence(list_sequence)

if __name__ == "__main__":
	main()