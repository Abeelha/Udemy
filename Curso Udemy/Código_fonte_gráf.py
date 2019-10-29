# Visualização de dados em Python
import matplotlib.pyplot as plt
 
x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 400, 400, 1000, 250] #tamanho
 
titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"
 
# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
 
plt.plot(x, y, color="#20B2AA", linestyle="-")
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=z) #
plt.legend()
plt.show()
plt.savefig("figura1.png", dpi=300)