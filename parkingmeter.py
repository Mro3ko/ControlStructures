time=int(input("Enter number of hours car was parked: "))
if time==0:
    fee=0
elif 1<=time<=2:
    fee=5
elif 3<=time<=6:
    fee=15
elif time>6:
    fee=20
print(f"total fee is {fee}PLN")