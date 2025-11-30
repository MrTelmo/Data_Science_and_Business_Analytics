#Exercicio 1
def saudacao(nome):
  print(f"Olá, {nome}!")

nome=input("Introduzir nome: ")
saudacao(nome)

#Exercicio 2
def soma(*args):
  return sum(args)

number_1=int(input("Input number: "))
number_2=int(input("Input another number: "))
print("Sum: ", soma(number_1,number_2))

#Exercicio 3
def average(*args):
  return (sum(args)/len(args))

number_1=int(input("Input number: "))
number_2=int(input("Input another number: "))
number_3=int(input("Input last number: "))
print("Average: ", average(number_1,number_2,number_3))

#Exercicio 4
def maior_numero(*args):
  return max(args)

number_1 = int(input("Input number: "))
number_2 = int(input("Input another number: "))
number_3 = int(input("Input last number: "))
print("Maior numero: ", maior_numero(number_1,number_2,number_3))

#Exercicio 5
quadrado = lambda x: x*x
number = int(input("Input number: "))
print(f"Quadrado de {number} -> ", quadrado(number))

#  ou
#  def quadrado(x):
#    return x*x
#  print(quadrado(3))

#Exercicio 6
#list_initial=[1,2,3,4,5]
list_defined = list(range(int(input("Defina o valor máximo da lista: "))+1))
print("Lista inicial -> ", list_defined)
list_doble = list(map(lambda x: x*2, list_defined))
print("Lista dobrada -> ", list_doble)

#Exercicio 7
#list_numeros=[1,2,3,4,5,6,7,8]
list_defined = list(range(int(input("Defina o valor máximo da lista: "))+1))
pares_list=list(filter(lambda x: x % 2 == 0, list_defined))
print(" # pares da lista -> ", pares_list)

#Exercicio 8
input_name=input("Introduzir nome: ")
input_age=input("Introduzir idade: ")
input_amount=input("Introduzir saldo: ")
def info_client(**kwargs):
  print(kwargs)
info_client(nome=input_name, age=input_age, saldo=input_amount)

#Exercicio 9
def somar_todos(*args):
  total=0
  for number in args:
    total += number
  return total

list_numbers = list(range(1,int(input("Defina o numero máximo list: "))+1))
print("List numbers: ",list_numbers)
print("Sum of list numbers: ", somar_todos(*list_numbers))

#ou mais simples
#print("Sum: ", somar_todos(1,3,6))

#Exercicio 10
def aplicar_imposto(valor, taxa=23):
  imposto = round(valor*(1+(taxa/100)),2)
  return imposto
valor=float(input("Introduzir montante: "))
taxa=(input("Introduzir taxa: "))
if taxa == "":
  print("Valor com taxa de 23% aplicada por defeito: ",aplicar_imposto(valor))
else:
  taxa=float(taxa)
  print(f"Valor com taxa de {taxa}% aplicada: ",aplicar_imposto(valor,taxa))


#ou mais simples
#def aplicar_imposto(valor, taxa=23):
#  imposto = round(valor*(1+(taxa/100)),2)
#  return imposto
#print("Valor com taxa: ",aplicar_imposto(100,0))
