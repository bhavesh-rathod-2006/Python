cost=int(input("Enter the cost price "))
selling_price=int(input("Enter the selling price "))

a=selling_price-cost
b=(a/cost)*100
if a>0:
    print(f"profit of {b} % ")

elif a<0:
    print(f"Loss of {-b} %")
else:
    print("No profit and No loss ")        