#primeiro projeto calculadora automática

Escolha1 = int(input("Escolha qual ação deseja: \n 1- Calculo simples \n 2- Cálculo com formulas \n Escolha: "))
if Escolha1 == 1:
print("Agora, escreva um número , operador e outro número")
#Cálculo Simples
número_simples1 = float(input("Digite o primeiro Número: "))
operador = input("Operadores Disponíveis: \n + = Adição \n - = Subtração \n * = Multiplicação \n / = Divisão \n **= Potência \n % = Módulo \n Escolha um Operador: ")
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
	print("O que você pretende calcular?")
Escolha2 = int(input("O que você quer calcular? \n 1- Perímetro e Área de figuras planas \n 2- "))
if Escolha2 == 1:
	print("coco")