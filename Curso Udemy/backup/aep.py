Escolha3 = int(input("\nEscolha Qual figura deseja calcular a àrea(de 1 face), perímetro(de 1 face) e volúme de base: \n 1- Quadrado(Cubo) \n 2- Retângulo(Paralelepípedo) \n 3- Triângulo(Pirâmide de base quadrada) \n 4- Trapézio(prisma) \n 5- Círculo(esféra) \n 6- Losango \nEscolha: "))
if Escolha3 == 1: #quadrado/cubo
	print("\nVocê escolheu quadrado/cubo")
	lado_qua = float(input("\nQual o valor do lado: "))
	peri_qua = lado_qua * 4 #perímetro
	area_qua = lado_qua ** 2 #área
	volu_qua = lado_qua ** 3 #volúme
	print("\nO perímetro da face quadrada é = ", peri_qua ,"\nA área é = ", area_qua , "\nO volúme é = ",volu_qua)
elif Escolha3 == 2: #Retangulo/paralelepípedo
	comp_ret = float(input("\nQual o valor do comprimento: "))
	larg_ret = float(input("\nQual o valor da lardura: "))
	alt_ret = float(input("\nQual o valor da altura: "))
	peri_ret = (2*comp_ret)+(2*alt_ret) #perímetro
	area_ret = comp_ret*alt_ret #área
	volu_ret = larg_ret*comp_ret*alt_ret #volúme
	print("\nO perímetro da face retangular é = ", peri_ret ,"\nA área da base é = ", area_ret,"\nO volúme é = ",volu_ret)
elif Escolha3 == 3: #Triângulo/Pirâmide
	base_tri = float(input("\nQual o valor da base: ")) #Base
	alt_tri = float(input("\nQual o valor da altúra: ")) #Altura
	arest_tri = (((base_tri/2)**2) + (alt_tri**2))**0.5 #Aresta
	peri_tri = base_tri + (2*arest_tri) #Perímetro
	area_tri = (base_tri*alt_tri)/2 #Àrea
	volu_tri = ((base_tri**2)*alt_tri)/3 # Volúme
	print ("\nO perímetro é = ", peri_tri , "\nA área é = ", area_tri , "\nO volúme é = ", volu_tri)
elif Escolha3 == 4: #Trapézio
	baseMA_trap = float(input("\nQual o valor da base maior: "))
	baseME_trap = float(input("\nQual o valor da base menor: "))
	alt_trap = float(input("\nQual o valor da altúra: "))
	larg_trap = float(input("\nQual o valor da largura: "))
	lado_trap = (((baseMA_trap - baseME_trap)/2)**2 + (alt_trap**2))**0.5
	peri_trap = baseMA_trap + baseME_trap + (lado_trap*2)
	area_trap = ((baseMA_trap + baseME_trap)*alt_trap)/2
	volu_trap = (((baseMA_trap + baseME_trap)*alt_trap)/2)*larg_trap
	print("\nO perímetro é = ", peri_trap ,"\nA área da face é = ", area_trap,"\nO volúme é = ",volu_trap)
elif Escolha3 == 5: #Círculo
	pi = 3.14 #Constante
	diam_cir = float(input("\nQual o valor do diâmetro: "))
	raio_cir = diam_cir/2
	peri_cir = (pi*2) * raio_cir
	area_cir = pi * (raio_cir**2)
	volu_cir = (4*pi*(raio_cir**3))/3
	print("\nO perímetro é = ", peri_cir ,"\nA área da face é = ", area_cir,"\nO volúme é = ",volu_cir)