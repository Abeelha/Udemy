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