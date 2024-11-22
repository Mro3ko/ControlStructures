a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if not  a<0 or not b<0:
    print(f"At least one of the numbers {a} and {b} is not negative")
else:
    print("Both numbers are negative")