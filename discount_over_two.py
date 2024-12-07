#input nr of products
#input price
#25% discount for each product over 2
num_of_products=int(input("Enter number of products purchased: "))
product_price=int(input("Enter product price: "))
total=0
if num_of_products<=2:
    total=num_of_products*product_price
else:
    total=2*product_price+(num_of_products-2)*40*0.75
print(f"Amount to pay: {total}")