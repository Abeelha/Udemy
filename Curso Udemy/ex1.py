#Idade
Idade = int(input("Digite sua idade "))
#Condição da idade
if Idade >= 18:
	print("Maior de idade")
elif 0 < Idade < 18:
	print ("Menor de idade")
else:
	print("idade inválida")

#Notas
Nota1 = float(input("Digite sua nota em Matemática "))
Nota2 = float(input("Digite sua nota em Filosofia "))

#Média
media = (Nota1 + Nota2)/2 
print ("Sua média é ", media)

if media >=6:
	print ("Aprovado!")
else:
	print ("Reprovado!")

#Equação de 2ndo grau

a = float(input("Digite valor de A "))
b = float(input("Digite valor de B "))
c = float(input("Digite valor de C "))

delta = b**2 - (4*a*c)
raiz_delta = delta**0.5

x1 = (-b+raiz_delta)/(2*a)
x2 = (-b-raiz_delta)/(2*a)

print(x1)
print(x2)
#Operaçao com input
num1 = float(input("Digite o primeiro Número: "))
operador = input("Digite o operador: ")
num2 = float(input("Digite o segundo Número: "))
#Soma 
if operador == "+":
	resultado = num1 + num2
#Subtração
elif operador == "-"
:	resultado = num1 - num2
#Divisão
elif operador == "/":
	resultado = num1 / num2
#Multiplicação
elif operador == "*":
	resultado = num1 * num2
#Potencia
elif operador == "**":
	resultado = num1 ** num2
#Módulo
elif operador == "%":
	resultado = num1 % num2
else:
	print("Uma falha aconteceu :/")
print (resultado)
