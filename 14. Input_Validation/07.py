available_ammout = int(input("Enter available ammount => "))

if  available_ammout>0 :
    withdrawal= int(input("Enter a withdrawal ammount => "))
    while withdrawal<0 or withdrawal>available_ammout :
        print(f"Invalid , withdrawal amount should be in Range 1 to {available_ammout}")
        withdrawal= int(input("Enter a withdrawal ammount => "))
        if withdrawal<= available_ammout and withdrawal>0:
            print("Accepted !!")
    if withdrawal<= available_ammout and withdrawal>0:
      print("Accepted !!")        

else:
    print("Available ammount should be greater than 0 ")           




