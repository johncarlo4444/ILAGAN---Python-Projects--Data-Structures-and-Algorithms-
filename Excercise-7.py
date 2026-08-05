print("==========Ilagan Python - Excercise 7==========")

print("\n==========Problem  1 :==========\n")

Firstnumber = (input("Enter first number: "))
Secondnumber = (input("Enter second number: "))
Sum = int(Firstnumber) + int(Secondnumber)
print("Sum      : ", Sum)
print("Joined   : ", Firstnumber + Secondnumber)

print("\n==========Problem  2 :==========\n")

Firstname = input("First Name: ")
Middlename = input("Middle Name: ")
Lastname = input("Last Name: ")

print(f"\nFull Name: {Firstname.upper()} {Middlename.upper()} {Lastname.upper()}")
print(f"Initials: {Firstname[0].upper()}.{Middlename[0].upper()}.{Lastname[0].upper()}.")

print("\n==========Problem  3 :==========\n")

Name = input("Enter your name: ")
Birthyear = int(input("Enter your birth year: "))

Currentyear = 2026
Age = Currentyear - Birthyear

print(f"\nName: {Name.upper()}")
print(f"Age: {Age} years old")

print("\n==========Problem  4 :==========\n")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sumresult = num1 + num2
diffresult = num1 - num2
prodresult = num1 * num2
quotresult = num1 / num2  # assume num2 != 0

print(f"\nSum = {sumresult:.2f}")
print(f"Difference = {diffresult:.2f}")
print(f"Product = {prodresult:.2f}")
print(f"Quotient = {quotresult:.2f}")