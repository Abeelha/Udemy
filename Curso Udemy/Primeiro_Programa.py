#Meu primeiro programa ( # quer dizer comentário )
"""
Comentário de várias linhas (3x")
Operadores----Operação
       +     =     Adição
       -     =     Subtração
       *     =     Multiplicação
       /     =     Divisão
       **    =     Potência
       %     =     Módulo
Operadores relacionais
       ==           igual
       !=           Diferente
       >            maior
       <            menor
       >=           maior igual
       <=           menor igual
Operadores Lógicos
    and        Duas condições sejam verdadeiras
    or         Pelo menos uma condição seja verdadeira
    not        Inverte o valor
"""
#Variáveis
var1 = 1                   # variável inteira
var2 = 3.14                # variável float
var3 = True                # boolean : true ou false
x=1
y=2
z=3
w=2
soma = x + y
print(soma <= y)
print(x == z or w == y)
if soma < x:                         #if = se ... entao true or false
	print("soma de x e y é MENOR que x")
elif soma!=x:                        #se if falhar , print elif
	print("soma é diferente que x")
else:                                # se elif falhar , print else
	print("x não é maior que a soma")

#While (enquanto)
while x < 10: #enquanto x maior que 10 , print ele 
	x+=1  # x = x + 1
	print(x)

#lista
lista1 = [1,2,3.14,4,5,"ola",True,"biscoito"] #lista1
for item in lista1:         # for = para
	print(item)
for item in range (1,10,2): # print de 1 a 10 pulando de 2 a 2
	print(item)
lista1.append("bolacha") # append (adicionar algo a lista)
print(lista1[8])         #print quem esta na posiçao x
if "bolacha" in lista1:  #se x esta na lista
  print("bolacha está na lista")
del lista1 [5:] #remove do item 5 até final
print (lista1)

lista2 = ["Z","A","D","B","T","I","S","G","T","Y","H","F","S","D","C"]
lista2.reverse() #inverte a sequencia da lista ultimo troca pelo primeiro...
print (lista2)
lista2.sort()  #coloca em ordem crescente
print (lista2)
lista2.sort(reverse=True) #coloca em ordem decrecente
print (lista2)

#Dicionário ( chaves e valores )
meu_dicionário = {"A":"Ameixa","B":"Bola","C":"Casa"} #A = chave q recebe valor de Ameixa
for chave in meu_dicionário:# . + values = print ameixa ; . + keys = print A
  print(chave+"-"+meu_dicionário[chave])
  
#strings
string1 = "EU SOU UMA STRING" # variável string
string2 = "kappa"             # outra string

concatenar = string1 +" " + string2  + "\n"  #junção de strings
print (concatenar)	
tamanho_string = len (concatenar) #conta quantos caracteres existem na var
print(tamanho_string)
print(string2[0],string2[1],string2[2],string2[3],string2[4]) # imprimir somente a numero q eu escolher
print(concatenar[0:6]) #imprimir até onde eu marcar
print(string1.lower()) #deixar string minúscula
print(string2.upper()) #deixar string maiúscula

#strings2
minha_string= "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split("r")#transforma uma sequencia em lista/quebra letra selecionada(case sensitive)
print(minha_lista)
busca=minha_string.find("rei") #find = busca local da palavra,se nao encontra a string = -1
print(minha_string[busca:])
minha_string=minha_string.replace("o rei","a rainha") #replace a string colocada por outra          
print(minha_string) 

"""
Input
String_input = input("Escreva string aqui ") #string
Número_inteiro = int(input("Digite seu número ")) #int = numeros como: 1,2,3...
Número_decimal = float(input("Digite seu número ")) #float = números como: 3.1415... ( use ponto no lugar de vírgula!!!)
print(String_input,"\n",Número_inteiro,"\n",Número_decimal)
"""

"""
FUNÇÕES definida pela palavra
--def NOME(PARÂMETROS):
  COMANDOS
--Chamada
NOME(ARGUMENTOS)

sempre colocar funções na parte de cima do código!
"""
def soma(x, y):
  return x+y
def multiplicação(x, y):
  return x*y

s = soma(2, 3) #2 + 3
m = multiplicação(3, 4) # 3 * 4

print(soma(s, m)) #Soma entre s = 2+3 & m = 3*4

#Números aleatórios
import random

n_randomint = random.randint(0, 10) #Números inteiros
n_randomfloat = random.uniform(0, 10) #Números decimais
print (n_randomint)
print(n_randomfloat)
#Random de lista
lista_random = [12,3.14,420,666]
n_lista_random = random.choice(lista_random)  #Choice usa para escolher algo em uma lista
print(n_lista_random)

#Exceções

dividendo = 2
divisor = 0
try:  #tente fazer isso...
  print(a/b)
except: #senão faça isso
  print("Não é permitida divisão por 0")
print(dividendo/dividendo) #continua compilação sem error

"""
BANCO DE DADOS:

MySQL é  Sistema Gerenciador de Banco de Dados (SGBD)
Principal tarefa de SGBD é gerenciar o acesso, manipulação e organização de dados

Comandos SQL:

-DDL (Definition Data Language):
Criar, alterar e apagar elementos do SGBD

-DML (Data Manipulation Language):
Recuperar, inserir, alterar ou apagar dados das tabelas
ou seja, para manipulação dos dados existentes

-DCL (Data Control Language):
Definir os privilégios de acesso aos dadods a cada usuário


TIPOS DE DADOS:
Números:
Inteiros:
  Tinyint - número inteiro muito pequeno
  smallint - número ineiro pequeno
  mediumint - número inteiro de tamanho médio
  int - número inteiro comum
  bigint - número inteiro grande
Decimais:
  decimal - número decimal , de ponto fixo
  float - número de ponto flutuante de precisao simples (32 bits)
  double - número de ponto flutuante de precisão dupla (64 bits)

Texto:
  Char - uma cadeia de caracteres (string), de tamanho fixo e nao binária
  varchar - uma string de tamanho variável e nao binária
  text - uma string nao binária e pequena

Data: Y = year / M = mês / D = day / h = hours / m = minutes / s = seconds
  Date - "YYYY-MM-DD"
  Time - "hh:mm:ss"
  datetime - "YYYY-MM-DD hh:mm:ss"


Apagando tabelas (CAUTION)
  DROP TABLE = deleta tabela 
  DROP DATABASE = deleta base de dados inteira


Inserir dados em tabela:
 INSERT INTO "table_name" (column1, column2 , ...)
 VALUES (value1, value2, value3, ...)
 (se o value for auto_increment , escrever "DEFAULT")

Alterar dados em tabela:
  UPDATE "table_name"
  SET column1 = value1, column2 = value2
  WHERE condition (id_pessoa = x)

Deletar dado em tabela:
  DELETE FROM "table_name"
  WHERE condition (id_pessoa = x)

Fazendo buscas:
  SELECT * (nome, cidade , data_nascimento , ...)
  FROM "table_name"
  WHERE cidade = "CURITIBA" (procurar somente quem mora em Curitiba)
  ORDER BY nome (ordem alfabética) /or/ ORDER BY nome DESC (ordem inversa)

Operadores lógicos
  SELECT *
  FROM "table_name"
  WHERE id_pessoa = x OR id_pessoa = y (OR recupera tanto 1 como outro)
  WHERE cidade = 'x' AND estado = 'y' (AND se tem id x e y ao mesmo tempo)
Operadores relacionais
  SELECT *
  FROM "table_name"
  WHERE data_nascimento >= '1990-01-01'
  OS OPERADORES SÃO : == ; = ; >= ; <= ; <> (diferente)