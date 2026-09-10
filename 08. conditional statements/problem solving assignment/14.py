cost=int(input("Enter the cost price "))
selling_price=int(input("Enter the selling price "))

a=selling_price-cost
if a>0:
    print(f"profit of {a} ")
elif a<0:
    print(f"Loss of {-a} ")
else:
    print("No profit and No loss ")        