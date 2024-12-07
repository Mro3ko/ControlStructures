pin= "0805"
for i in range (1,5):
    if i==4:
        print()
        print("Sorry your card has been blocked.")
    user_pin=input("Enter the PIN code: ")
    if user_pin==pin:
        print("Correct")
        break
    else:
        print("Incorrect...")