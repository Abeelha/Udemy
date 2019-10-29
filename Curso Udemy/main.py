import aleatorio as a
import media as m

lista = a.geraListaInteiro(5) #tamanho da lista = 10

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)



print(lista)
print("A média da lista é "+ str(media))
print("A mediana da lista é "+ str(mediana))
print("A moda da lista é "+ str(moda))