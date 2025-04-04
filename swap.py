# Implement a program that swaps the values of two variables.

a = int(input("enter your number: "))
b = int(input("enter another number: "))

temp = a
a = b
b = temp

print(f"now your a value is {a} and b  value is {b}")