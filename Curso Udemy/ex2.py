#comparar sequencias
seq1 = input("Digite sua sequência 1: ")
seq2 = input("Digite sua sequência 2: ")

if seq1 == seq2:
	print("São iguais!")
elif seq1 != seq2:
	print("São diferentes")
else:
	print("Inválido!")


#arquivo sequencia
nome = input("Digite o nome que deseja abrir: ")

arquivo = open(nome)

linhas = arquivo.readlines()

for linha in linhas:
	print (linha.strip()) #strip remove caracteres especiais

#receba seq digitada e salve em arquivo

seq = input("Digite uma sequencia: ")

arquivo2 = open("seq2.fasta","w")

arquivo2.write(">seq\n")
arquivo2.write(seq)

arquivo2.close()

#Menu
menu = 0

def abrirArquivo():
	nome = input("Digite nome do arquivo que deseja abrir: ")

	arquivo3 = open(nome)

	return arquivo3

def lerArquivo(arquivo3):
	linhas2 = arquivo.readlines()

	for linha2 in linhas2:
		print (linha2.strip())

while menu != 3:
	print ("(1) Abrir arquivo\n(2) Ler arquivo aberto\n(3) Sair\n")
	menu = int(input("Digite a opção desejada: "))

	if menu == 1:
		arquivo3 = abrirArquivo()
	elif menu == 2:
		lerArquivo(arquivo3)

#Program q leia multifasta e armazena como dicionario

arquivo = open("seq.fasta")

linhas3 = arquivo.readlines()
multifasta = {}

for linha3 in linhas3:
	if linha3[0] == ">":
		seq_atual = linha3[1:].strip()
		multifasta[seq_atual] = ""
	else:
		multifasta[seq_atual] = multifasta[seq_atual] + linha3.strip()

print(multifasta["seq3"])




