unit = int(input("""  Chose your account from menu 
1 → Savings
2 → Current
==> """))


amount = int(input("Enter a ammout if you want to withdraw "))

match unit :
    case 1 :
        if amount>0 :
            print(" Continue ")
        else :
            print("Invalid ammount")
    case 2 :
         if amount>0 :
             print(" Continue ")
         else :
              print("Invalid ammount")
    case _ :
        print("Select a valid value from menu ")          
