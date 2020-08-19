'''
Instituto Federal de Brasília - Campus: Taguatinga
Aluna: Danyelle da Silva Oliveira Angelo.
Professor: João Victor de Oliveira Araújo - Disciplina: Bioinformática - 2020
'''
def fatorial(numero):
	fat = 1
	for i in range(numero,-0,-1):
		fat = fat * i
	return fat

def main():
	n = int(input("Entrada:"))
	print("Saída: %d" %(fatorial(n)))

if __name__ == "__main__":
	main()