EnterAge = int(input("Enter your Age: "))

if EnterAge >= 60:
    print("You are a senior citizen.")
elif EnterAge >= 18 and EnterAge <= 59:
    print("You are an adult.")
elif EnterAge >= 13 and EnterAge <= 17:
    print("You are a teenager.")
elif EnterAge >= 0 and EnterAge <= 12:
    print("You are a child.")
else:
    print("Invalid age.")