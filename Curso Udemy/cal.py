#primeiro projeto calculadora automática
Escolha1 = int(input("Escolha qual ação deseja: \n 1- Calculo simples \n 2- Cálculo com formulas \n Escolha: "))
try:
	if Escolha1 == 1:
		print("Agora, escreva um número , operador e outro número")
		#Cálculo Simples
		número_simples1 = float(input("\nDigite o primeiro Número: "))
		operador = input("\nOperadores Disponíveis: \n +  Adição \n -  Subtração \n *  Multiplicação \n /  Divisão \n ** Potência \n %  Módulo \n Escolha um Operador: ")
		número_simples2 = float(input("\nDigite o segundo Número: "))
		#Soma 
		if operador == "+":
			resultado = número_simples1 + número_simples2
		#Subtração
		elif operador == "-":
			resultado = número_simples1 - número_simples2
		#Divisão
		elif operador == "/":
			resultado = número_simples1 / número_simples2
		#Multiplicação
		elif operador == "*":
			resultado = número_simples1 * número_simples2
		#Potencia
		elif operador == "**":
			resultado = número_simples1 ** número_simples2
		#Módulo
		elif operador == "%":
			resultado = número_simples1 % número_simples2
		else:
			print("Uma falha aconteceu :/")
		print (resultado)
	elif Escolha1 == 2:
		print("\nVocê escolheu calculo com fórmulas")
		Escolha2 = int(input("\nQual cálculo deseja: \n 1- Figuras geométricas \n ... "))
		if Escolha2 == 1:
			print("\nVocê escolheu calcular figuras geométricas")
			#escolha_Área,Perímetro e Volúme
			Escolha_APV = int(input("\nEscolha Qual figura deseja calcular a àrea, perímetro(de 1 face) e volúme: \n 1- Quadrado(Cubo) \n 2- Retângulo(Paralelepípedo) \n 3- Triângulo(Pirâmide de base quadrada) \n 4- Trapézio(Prisma) \n 5- Círculo(Esféra) \n 6- Losango(Octaedro) \nEscolha: "))
			#quadrado/cubo
			if Escolha_APV == 1:
				print("\nVocê escolheu quadrado/cubo")
				lado_qua = float(input("\nQual o valor do lado: "))
				peri_qua = lado_qua * 4 #perímetro				area_qua = lado_qua ** 2 #área				volu_qua = lado_qua ** 3 #volúme
				print("\nO perímetro da face quadrada é = ", peri_qua ,"\nA área é = ", area_qua , "\nO volúme é = ",volu_qua)
			#Retangulo/paralelepípedo
			elif Escolha_APV == 2:
				print("\nVocê escolheu Retangulo/paralelepípedo")
				comp_ret = float(input("\nQual o valor do comprimento: "))
				alt_ret = float(input("\nQual o valor da altura: "))
				larg_ret = float(input("\nQual o valor da lardura: "))
				peri_ret = (2*comp_ret)+(2*alt_ret) #perímetro
				area_ret = comp_ret*alt_ret #área
				volu_ret = larg_ret*comp_ret*alt_ret #volúme
				print("\nO perímetro da face retangular é = ", peri_ret ,"\nA área da base é = ", area_ret,"\nO volúme é = ",volu_ret)
			#Triângulo/Pirâmide
			elif Escolha_APV == 3:
				print("\nVocê escolheu Triângulo/Pirâmide")
				base_tri = float(input("\nQual o valor da base: ")) #Base
				alt_tri = float(input("\nQual o valor da altúra: ")) #Altura
				arest_tri = (((base_tri/2)**2) + (alt_tri**2))**0.5 #Aresta
				peri_tri = base_tri + (2*arest_tri) #Perímetro
				area_tri = (base_tri*alt_tri)/2 #Àrea
				volu_tri = ((base_tri**2)*alt_tri)/3 # Volúme
				print ("\nO perímetro é = ", peri_tri , "\nA área é = ", area_tri , "\nO volúme é = ", volu_tri)
			#Trapézio/Prisma
			elif Escolha_APV == 4:
				print("\nVocê escolheu Trapézio/Prisma")
				baseMA_trap = float(input("\nQual o valor da base maior: "))
				baseME_trap = float(input("\nQual o valor da base menor: "))
				alt_trap = float(input("\nQual o valor da altúra: "))
				larg_trap = float(input("\nQual o valor da largura: "))
				lado_trap = (((baseMA_trap - baseME_trap)/2)**2 + (alt_trap**2))**0.5
				peri_trap = baseMA_trap + baseME_trap + (lado_trap*2)
				area_trap = ((baseMA_trap + baseME_trap)*alt_trap)/2
				volu_trap = (((baseMA_trap + baseME_trap)*alt_trap)/2)*larg_trap
				print("\nO perímetro é = ", peri_trap ,"\nA área da face é = ", area_trap,"\nO volúme é = ",volu_trap)
			#Círculo/Esféra
			elif Escolha_APV == 5:
				print("\nVocê escolheu Círculo/esféra")
				pi = 3.14 #Constante
				diam_cir = float(input("\nQual o valor do diâmetro: ")) #Calcula o raio
				raio_cir = diam_cir/2 #raio
				peri_cir = (pi*2) * raio_cir #perímetro
				area_cir = pi * (raio_cir**2) #área
				volu_cir = (4*pi*(raio_cir**3))/3 #volúme
				print("\nO perímetro é = ", peri_cir ,"\nA área da face é = ", area_cir,"\nO volúme é = ",volu_cir)
			#Losango/Octaedro
			elif Escolha_APV == 6: 
				diagMA_los = float(input("\nQual o valor da diagonal maior: "))
				diagME_los = float(input("\nQual o valor da diagonal menor: "))
				area_los = (diagMA_los*diagME_los)/2 #área
				lado_los = (((diagMA_los/2)**2)+((diagME_los/2)**2))**0.5 #aresta/lado
				peri_los = 4*lado_los #perímetro
				volu_los = ((lado_los**3)*(2**0.5))/3 #Volúme
				print("\nO perímetro é = ", peri_los ,"\nA área da face é = ", area_los,"\nO volúme é = ",volu_los)
			else:
				print("\nNúmero inválido")
		elif Escolha2 == 2:
			print("coco")
		else:
			print("Número inválido")
	else:
		print("\nNúmero inválido")
# except:
# 	print("Escolha inválida")
except Exception as e:
	raise e
