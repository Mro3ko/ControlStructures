amount=int(input("Enter the amount: "))
print("The amount of {amount}PLN in coins:")

count_5=amount//5
amount=amount%5

count_2=amount//2
amount=amount%2

count_1=amount

if count_5 > 0:
    print(f"5 PLN coins: {count_5}")
if count_2 > 0:
    print(f"2 PLN coins: {count_2}")
if count_1 > 0:
    print(f"1 PLN coins: {count_1}")