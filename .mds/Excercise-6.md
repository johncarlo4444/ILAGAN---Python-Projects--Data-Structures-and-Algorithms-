print("==========Ilagan Python - Excercise 6==========")
print("\n==========STUDENT Information==========\n")

Firstname = input("Enter your First Name: ")
Middlename = input("Enter your Middle Name: ")
Lastname = input("Enter your Last Name: ")
Subd = input("Enter your Subdivision/Sitio/House No.: ")
Brgy = input("Enter your Barangay: ")
Muni = input("Enter your Municipality: ")
Prov = input("Enter your Province: ")
Course = input("Enter your Course: ")
YearLevel = input("Enter your Year Level: ")
EmailAdd = input("Enter your Email Address: ")

Fullname = Firstname +" "+ Middlename +" "+ Lastname 
Address = Subd +" "+ Brgy +" "+ Muni +" "+ Prov

print("\n==========STUDENT Information==========\n")

print("Full Name    : " , Fullname)
print("Address      : " , Address)
print("Course       : ", Course)
print("Year Level   : " , YearLevel)
print("Email Address: ", EmailAdd)

print("\n==========Water Bill==========\n")

Name = input("Enter Customer's Name: ")
PreviousReading = input("Enter Previous Meter Reading: ")
CurrentReading = input("Enter Current Meter Reading: ")
Rate = input("Enter Rate per cubic meter: ")

PreviousReading = float(PreviousReading)
CurrentReading = float(CurrentReading)
Rate = float(Rate)
ConsumedUnits = CurrentReading - PreviousReading
TotalBill = float(ConsumedUnits * Rate)
 
print("\n==========CUSTOMER'S BILL==========\n")

print ("Customer's Name: " , Name)
print ("Customer's Consumed Units: " , f"{ConsumedUnits:.2f}", "cubic meter")
print ("Customer's Total Bill is Php " +  f"{TotalBill:.2f}" )