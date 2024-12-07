decimal_num=int(input("Enter a number: "))
result=""
num=decimal_num
while num>0:
    result=str(num%2)+result
    num=num//2
print(f"{decimal_num}(10)={result}(2)")