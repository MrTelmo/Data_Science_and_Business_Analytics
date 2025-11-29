# Exercicio 1 - Choose a number N and show every iteration from 1 until N.
N = int(input("Input an integer number: "))
for i in range(1, N + 1, 1):
    print(i)
    
# Exercicio 2 - Choose a number and showcase regressive countdown until 0.
N = int(input("Input an integer number: "))
for i in range(N, -1, -1):
    print(i)

# Exercicio 3 - Choose numbers randomly and sum them until user inputs 0, then showcase total sum of the input numbers.
number = int(input("Input number: "))
sum = 0
while number != 0:
  sum += number
  number = int(input("Input number: "))
print("Total sum:", sum)

# Exercicio 4 - Choose a number N and showcase the multiplication table of N.
number = int(input("Input number: "))
for i in range(1,11):
  multi_table = number*i
  print(number,"x",i,"=", multi_table)

# Exercicio 5 - Choose a number N and showcase the multiplication table from 1 to N.
number_table = int(input("Input number: "))
for i in range (1,number_table+1):
  for j in range(1,11):
    multi_table = j*i
    print(i,"x",j,"=", multi_table)
  print("-----------------------")

# Exercicio 6 - Choose a number N and showcase all even numbers until N inclusive.
even_number = int(input("Input number: "))
list=[x for x in range (0,even_number+1) if x%2==0]
print(list)

# Exercicio 7 - Choose a number N and showcase all the square from 1 until N inclusive.
square_number = int(input("Input number: "))
list=[x**2 for x in range (1,square_number+1)]
print(list)

# Exercicio 8 - From the list fruits
fruits = ["apple", "banana", "orange", "kiwi", "grape", "mango"]
# 8.1 - Print first 3 fruits
print(frutas[:3])
# 8.2 - Print last 3 fruits
print(frutas[-3:])
# 8.3 - Print the list inverted
print(frutas[::-1])

# Exercicio 9 - Input a word, and count the number of vowels in it.
word = input("Input word: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u','á', 'é', 'í', 'ó', 'ú','â', 'ê', 'î', 'ô', 'û','ã', 'õ']
count = 0
for letter in word:
  if letter in vowels:
    count += 1
print("# of vowels: ", count)

# Exercicio 10 -  TO BE continued
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

