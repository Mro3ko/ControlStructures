temp=int(input("Enter current temperature: "))
if temp>35:
    print("It is extremely hot")
elif temp>30:
    print("It is hot")
elif temp>=15:
    print("It is warm")
elif temp>=0:
    print("It is cold")
elif temp<0:
    print("Warning, frost!")