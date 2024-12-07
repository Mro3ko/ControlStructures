n=int(input("How many prime numbers to print: "))
d=n//2
for i in range(1,d+1):
    if n%d==0:
        print(f"{n} is not a prime number")
        break
