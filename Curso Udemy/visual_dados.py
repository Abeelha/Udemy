# Visualizacao de dados em Python

import matplotlib.pyplot as plt
import random

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [4, 2, 1, 7, 5]
z = [200, 400, 400, 1000, 250] #tamanho

titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
"""
#plt... (plot = linha) , (bar = barras), (pode juntar plot + scatter = pontos)
plt.plot(x1, y1, color="#20B2AA", linestyle="-")
plt.scatter(x2, y2, label="Meus pontos", color="k", marker=".", s=z) #s = tamanho (variavel z)
plt.legend()
plt.show() #mostrar grafico
plt.savefig("figura1.png", dpi=300) #savefig = save ; pode salvar em "pdf" ; quanto maior dpi , mais qualidade
"""

"""
label:	rótulo

linewidth: largura da linha


(color)

'b'	blue

'g'	green

'r'	red

'c'	cyan

'm'	magenta

'y'	yellow

'k'	black

'w'	white


Marcadores (marker)
'.'	point marker

','	pixel marker

'o'	circle marker

'v'	triangle_down marker

'^'	triangle_up marker

'<'	triangle_left marker

'>'	triangle_right marker

'1'	tri_down marker

'2'	tri_up marker

'3'	tri_left marker

'4'	tri_right marker

's'	square marker

'p'	pentagon marker

'*'	star marker

'h'	hexagon1 marker

'H'	hexagon2 marker

'+'	plus marker

'x'	x marker

'D'	diamond marker

'd'	thin_diamond marker

'|'	vline marker

'_'	hline marker


Tipos de linha (linestyle)
'-'	solid line style

'--'	dashed line style

'-.'	dash-dot line style

':'	dotted line style
"""

#boxplot

vetor = []

for i in range(10):
	numero_aleatorio = random.randint(0,5)
	vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()