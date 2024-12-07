a=int(input("Enter a number of a biggest row: "))
i=1
while i<=a:
    print(i*"*")
    i+=1
i-=2
while i>0:
    print(i*"*")
    i-=1
