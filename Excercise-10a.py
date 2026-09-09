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
	if Second == 0:
		print("Cannot divide by zero.")
	else:
		print("Result : ",First / Second)
else:
	print("Invalid operator")


