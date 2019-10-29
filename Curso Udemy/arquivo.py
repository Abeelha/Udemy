"""
Manipular arquivos
Função open(nome, modo)***
  Modos		Função:
	r 		somente leitura

	w 		escrita(caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)

	a 		leitura e escrita( adc o novo conteúdo ao fim do arquivo)

	r+ 		leitura e escrita

	w+ 		escrita( o modo w+, assim como o w , também apaga o conteúdo anterior do arquivo)

	a+  	leitura e escrita(abre o arquivo para atualização)+

 Lendo arquivos
	Read()  - lê arquivo inteiro
	Readline() - Lê uma linha
	Readlines() - Lê arquivo e o armazena em uma lista
"""
arquivo = open("arquivo.txt")
linhas = arquivo.readlines() # lê todas linhas e faz uma lista
print (linhas)
for linha in linhas:      #for = lê linha por linha
	print(linha)

escrever = open("arquivo.txt","a") # w cria novo arquivo
escrever.write("ola meu arquivo , voce nasceu muahahahaha! \n")
escrever.close()