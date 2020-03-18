import csv
entrada = open("uniprot-toxin+organism_spider+AND+reviewed_no.txt","r")
saida = open("saida.txt", "w")
erro = [] #grava as linhas que obtivemos algum erro
saida.write("AC \t \t \t \t DE")
leitor = csv.reader(entrada,delimiter=' ') #a cada "," encontrada no meu arquivo temos uma nova palavra
for row in leitor:
    if (row[0] == "AC"):
        row[3] = row[3].strip(";")
        saida.write("\n"+ row[3])
    if (row[0] == "DE" and row[3]=="SubName:"):
        row[4] = row[4].strip("Full=")
        saida.write("\t \t")
        saida.write(' '.join(row[4:])) #converte a lista em string
        saida.write(";")
entrada.close()
saida.close()
