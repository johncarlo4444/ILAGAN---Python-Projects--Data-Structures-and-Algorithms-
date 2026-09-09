print("ILAGAN PYTHON PROJECT EXCERCISE 8a")
print("\n1. CURRENCY CONVERTER\n")

LastName = input("Enter Last name: ")
FirstName = input("Enter First name: ")
MiddleName = input("Enter Middle name: ")

Fullname = FirstName + " " + MiddleName[0] + ". " + LastName

AmountPhilippinepesos = input("Enter Amount in Php: ")
PtoUSDexchangerate = input("Enter PHP-to-USD exchange rate: ")
PtoEURexchangerate = input("PHP-to-EUR exchange rate: ")

AmountPhilippinepesos = float(AmountPhilippinepesos)
PtoUSDexchangerate = float(PtoUSDexchangerate)
PtoEURexchangerate = float(PtoEURexchangerate)

USDollar = AmountPhilippinepesos / PtoUSDexchangerate
EURo = AmountPhilippinepesos / PtoEURexchangerate

print("Name: ", Fullname.upper())
print(f"Php: {AmountPhilippinepesos:.2f}")
print(f"USD: {USDollar:.2f}")
print(f"EUR: {EURo:.2f}")

print("\n2. STRING LENGTH CHALLENGE\n")

LastName = input("Enter Last name: ")
FirstName = input("Enter First name: ")
MiddleName = input("Enter Middle name: ")

Fullname = FirstName + " " + MiddleName[0] + ". " + LastName

print("Full name: ", Fullname)  
print("First name characters: ", str(len(FirstName.replace(" ",""))))
print("Middle name characters: ", str(len(MiddleName.replace(" ","")))) 
print("Last name characters: ", str(len(LastName.replace(" ",""))))
print("Total Characters: ", str(len(Fullname.replace(" ",""))))


