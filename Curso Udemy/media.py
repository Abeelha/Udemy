# media , mediana , moda
#from statistics import * maneira facil d fazer




def media(lista):
	#media = mean(lista) facil
	media = sum(lista)/float(len(lista))

	return media

def mediana(lista):
	#mediana = median(lista) facil
	lista_ordenada = sorted(lista)
	t = len(lista_ordenada)

	if t % 2 == 0:
		mediana = (lista_ordenada[int(t/2)] + lista_ordenada[int((t/2)-1)])/2
	elif t % 2 == 1:
		mediana = lista_ordenada[int(t/2)]

	return mediana

def moda(lista):
	#moda = mode(lista):
	lista_dic = {}

	for l in lista:
		if l not in lista_dic:
			lista_dic[l] = 1
		else:
			lista_dic[l] += 1

	maior_repeticao = max(lista_dic.values())

	for i in lista_dic:
		if lista_dic[i] == maior_repeticao:
			moda = i

	return moda
