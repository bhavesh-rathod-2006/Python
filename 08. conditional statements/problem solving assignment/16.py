bill=int(input("Enter the unit you used "))
if bill>0:
    if  0<=bill<=100:
        print(bill*5,"is the amount you should pay " )
    elif 100<bill<=200:
        print(500+((bill-100)*7)," is the amount you should pay ")
    else:
        print(1200+((bill-200)*10),"is the amount you should pay ")    
else:
    print("if you want to check you bill amount , then enetr a valid unit ")    






