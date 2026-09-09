print("ILAGAN PYTHON PROJECT EXCERCISE 8a")
print("\nComplex Number Operations\n")

Realpart1 = float(input("Enter real part of first number: "))
Imaginarypart1 = float(input("Enter imaginary part of first number: "))
Realpart2 = float(input("Enter real part of second number: "))
Imaginarypart2 = float(input("Enter imaginary part of second number: "))

FirstComplex = complex(Realpart1, Imaginarypart1)
SecondComplex = complex(Realpart2, Imaginarypart2)

Sum = FirstComplex + SecondComplex
Difference = FirstComplex - SecondComplex
Product = FirstComplex * SecondComplex
Quotient = FirstComplex / SecondComplex

print("\nOutput \n")

print("First Complex Number: ", FirstComplex)
print("Second Complex Number:  ", SecondComplex)

print("Sum: ", Sum)
print("Difference: ", Difference)
print("Product: ", Product)
print("Quotient: ", Quotient)