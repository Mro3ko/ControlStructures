age=int(input("How old are you: "))
if age<0:
    print("You did not enter a valid number!")
elif age<13:
    print("You are a child")
elif age<20:
    print("You are a teen")
elif age<65:
    print("You are an adult")
elif age>=65:
    print("You are a senior")
