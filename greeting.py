#Create a program that takes a user's name and age asinput and prints a greeting message

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))

if age >= 18:
    print(f"Hi {name}, your age is now {age} \nWelcome to Adulthood!")
else:
    print(f"Hi {name}, Your age is just {age} \nbecome Adult you Mother fucker!")