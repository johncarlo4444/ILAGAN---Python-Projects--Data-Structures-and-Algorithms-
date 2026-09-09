First = float(input("Enter first number: "))
Second = float(input("Enter second number: "))
Operator = input("Enter operator: ")

if Operator == "+":
	print("Result : ",First + Second) 
elif Operator == "-":
	print("Result : ",First - Second) 
elif Operator == "*":
	print("Result : ",First * Second) 
elif Operator == "/":
	print("Result : ",First / Second) 
else:
	print("Invalid operator")


