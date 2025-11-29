# Exercicio 1 - Choose a number N and show every iteration from 1 until N.
N = int(input("Input an integer number: "))
for i in range(1, N + 1, 1):
    print(i)
    
# Exercicio 2 - Choose a number and showcase regressive countdown until 0.
N = int(input("Input an integer number: "))
for i in range(N, -1, -1):
    print(i)

# Exercicio 3 - Peça números ao usuário até ele digitar 0. Mostre a soma total dos números digitados.
number = int(input("Input number: "))
sum = 0
while number != 0:
  sum += number
  number = int(input("Input number: "))
print("Total sum:", sum)

#exercicio 4
number = int(input("Input number: "))
for i in range(1,11):
  tabuada = number*i
  print(number,"x",i,"=", tabuada)

#exercicio 5
number_tabuada = int(input("Input number tabuada: "))
for i in range (1,number_tabuada+1):
  for j in range(1,11):
    tabuada = j*i
    print(i,"x",j,"=", tabuada)
  print("-----------------------")

#exercicio 6
list=[x for x in range (0,21) if x%2==0]
print(list)

#exercicio 7
list=[x**2 for x in range (1,11)]
print(list)

#exercicio 8
frutas = ["maçã", "banana", "laranja", "kiwi", "uva", "manga"]
print(frutas[:3])
print(frutas[-3:])
print(frutas[::-1])

#exercicio 9
word = input("Input word: ").lower()
#vogais = ["a","A","e","E","i","I","o","O","u","U"]
vogais = ['a', 'e', 'i', 'o', 'u','á', 'é', 'í', 'ó', 'ú','â', 'ê', 'î', 'ô', 'û','ã', 'õ']
count = 0
for letra in word:
  if letra in vogais:
    count += 1
print("# de Vogais:", count)

#exercicio 10
list=[4,7,1,9,3,10]
sum = 0
for i in list:
  sum += i
print(sum)

max = list[0]
min = list[0]
for num in list[0:]:
  if num > max:
    max = num
  if num < min:
    min = num
print("Max :",max)
print("Min :",min)

