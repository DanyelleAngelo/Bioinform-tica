'''
Instituto Federal de Brasília - Campus: Taguatinga
Aluna: Danyelle da Silva Oliveira Angelo.
Professor: João Victor de Oliveira Araújo - Disciplina: Bioinformática - 2020
'''
def subsequence(sequence):
	size = 4
	size_sequence = len(sequence)
	sub = {}
	for c in range(size_sequence - size + 1):
		key = sequence[c:c+size]
		if key in sub:
			sub[key] += 1
		else:
			sub[key]=1
	return len(sub)

def main():
	sequence = input("Entrada:")
	print("Saída: %d " %(subsequence(sequence)))

if __name__ == "__main__":
	main()