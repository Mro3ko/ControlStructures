total_sum = 0
n=0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break
    total_sum += number
    n+=1

arthimetic_mean=total_sum/n

print(f"The total sum of the numbers is: {total_sum}")
print(f"The arithmetic mean of the numbers is {arthimetic_mean}")