age=int(input("Enter dog's age in human years: "))
if age<=2:
    dogs_age=age*10.5
else:
    dogs_age=2*10.5+(age-2)*4
print(f"The dogs's age in dog's years is {dogs_age} years ")