import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:

    if countdown==5:
        print("five")
        countdown-=1
        time.sleep(1)
        continue

    elif countdown==4: 
        print("four")
        countdown-=1
        time.sleep(1)
        continue

    elif countdown==3: 
        print("three")
        countdown-=1
        time.sleep(1)
        continue

    elif countdown==2: 
        print("two")
        countdown-=1
        time.sleep(1)
        continue

    elif countdown==1: 
        print("one")
        countdown-=1
        time.sleep(1)
        continue
    
    print(countdown)
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")