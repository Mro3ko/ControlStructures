current_price=float(input("Current product price: "))
previous_price=float(input("Previous product price: "))
discount=previous_price-current_price
discount_percent=discount/previous_price*100
if discount_percent>=10:
    print("Buy the product!!")
    print(f"Product price reduced by {round(discount_percent)}%")
