# Exercicio 1 - Create a salutation function
def salutation(name):
  print(f"Hey, {name}!")
name=input("Input name: ")
salutation(name)

# Exercicio 2 - Create a function that sums numbers
def sum_numbers(*args):
  return sum(args)
number_1=int(input("Input number: "))
number_2=int(input("Input another number: "))
print("Sum: ", sum_numbers(number_1,number_2))

#Exercicio 3 - Create a function that sums 3 different numbers and returns the average.
def average(*args):
  return (sum(args)/len(args))
number_1=int(input("Input a number: "))
number_2=int(input("Input another number: "))
number_3=int(input("Input last number: "))
print("Average: ", average(number_1,number_2,number_3))

# Exercicio 4 - Create a function that identifies the largest number.
def max_number(*args):
  return max(args)
number_1 = int(input("Input a number: "))
number_2 = int(input("Input another number: "))
number_3 = int(input("Input last number: "))
print("Max number: ", max_number(number_1,number_2,number_3))

# Exercicio 5 - Create a function that can calculate the square of a number.
square = lambda x: x*x
number = int(input("Input a number: "))
print(f"The square of {number} -> ", square(number))
#  or
#  number = int(input("Input a number: "))
#def square(number):
#  return number*number
#print(f"The square of {number} -> ", square(number))

# Exercicio 6 - Create a function that generates a list of numbers from 0 to N, and then doubles the numbers in it in another list.
list_defined = list(range(int(input("Define max value of the list: "))+1))
print("List -> ", list_defined)
list_doble = list(map(lambda x: x*2, list_defined))
print("List Doubled -> ", list_doble)

# Exercicio 7 - Create a function that identifies the even numbers of a list with max number N.
list_defined = list(range(int(input("Define max value of the list: "))+1))
even_list=list(filter(lambda x: x % 2 == 0, list_defined))
print("Even #s of the list-> ", even_list)

# Exercicio 8 - Create a function that generate a dictionary with client informations.
input_name=input("Input name: ")
input_age=input("Input age: ")
input_amount=input("Input salary: ")
def info_client(**kwargs):
  print(kwargs)
info_client(name=input_name, age=input_age, salary=input_amount)

# Exercicio 9 - Create a function that sum all numbers from 1 to N.
def sum_all(*args):
  total=0
  for number in args:
    total += number
  return total
list_numbers = list(range(1,int(input("Define max number of the list: "))+1))
print("List numbers: ",list_numbers)
print("Total sum of list numbers: ", sum_all(*list_numbers))

# Exercicio 10 - Create a functinos that can calculate the price with VAT included. If no tax defined 23% applied by default, otherwise specified by the user.
def vat(value, tax_value=23):
  tax = round(value*(1+(tax_value/100)),2)
  return tax
value=float(input("Input amount: "))
tax_value=(input("Input tax value: "))
if tax_value == "":
  print("Total amount with VAT included. Applied 23% by default: ",vat(value))
else:
  tax_value=float(tax_value)
  print(f"Total amount with VAT of {tax_value}% included: ",vat(value,tax_value))

