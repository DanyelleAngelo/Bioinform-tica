'''
Instituto Federal de Brasília - Campus: Taguatinga
Aluna: Danyelle da Silva Oliveira Angelo.
Professor: João Victor de Oliveira Araújo - Disciplina: Bioinformática - 2020
'''
def subsequence(sequence):
	size = 3
	size_sequence = len(sequence)
	sub_seq = {}

	for c in range(size_sequence - size + 1):
		key = sequence[c:c+size]
		if key in sub_seq:
			sub_seq[key] += 1
		else:
			sub_seq[key]=1

	key = max(sub_seq, key=sub_seq.get)  # maximum value
	return key,sub_seq[key]

def readFile():
	filename = "sequence.fasta"
	list_sequence = []

	with open(filename, 'r') as fp:

		for header,sequence in  zip(fp,fp):
			header = header.replace("\n","")
			sequence = sequence.replace("\n","")
			sub_seq, n =subsequence(sequence)
			list_sequence.append((header,sub_seq,n))

	return list_sequence

def writeSequenceToFile(list_sequence):
	filename = "results.txt"
	with open(filename,"w") as fp:
		for header, sequence, n in list_sequence:
			fp.write("%s %s %s \n" %(header, sequence,n))

def main():
	list_sequence = readFile()
	writeSequenceToFile(list_sequence)

if __name__ == "__main__":
	main()