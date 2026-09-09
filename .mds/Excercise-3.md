FirstName = "John Carlo "
MiddleName = "Albos "
LastName = "Ilagan"
FullName = FirstName + MiddleName + LastName

print("Ako si " + FullName)
print(FullName.upper())
print(FullName.lower())
print("Number of characters (no spaces): "  + str(len(FullName.replace(" ", ""))) ) 
print(FirstName[:3])
print(LastName[1:])
print(FirstName[0]+"."+FirstName[5]+"."+ MiddleName[0]+"."+LastName[0]+".")

