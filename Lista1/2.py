'''
Instituto Federal de Brasília - Campus: Taguatinga
Aluna: Danyelle da Silva Oliveira Angelo.
Professor: João Victor de Oliveira Araújo - Disciplina: Bioinformática - 2020
'''
def calculateGc(sequence):
	try:
		base_n = {'a':0,'t':0,'c':0,'g':0}
		size = len(sequence)
		result = 0
		for c in range(size):
			key = sequence[c].lower()
			if key in base_n:
				base_n[key] += 1
	
		result = ((base_n['g']+base_n['c'])/(base_n['a']+base_n['t']+base_n['g']+base_n['c']))*100	
		return ("%d%%" %(result))

	except ZeroDivisionError:
		return('Erro: não existe nenhuma base nitrogenada na sequência - divisão por zero')

def main():
	sequence = input("Entrada:")
	print("Saída: %s " %(calculateGc(sequence)))

if __name__ == "__main__":
	main()