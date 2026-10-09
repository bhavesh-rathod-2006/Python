method = int(input("""Select a payment method 
1 → UPI
2 → Card
3 → Wallet
=>   """))


match method:
    case 1 :
        choose = int(input("""Select a option from below
1 → Scan QR
2 → Enter UPI ID
=>   """)) 
        match choose :
            case 1 :
                print("QR is selected")
            case 2:
                print("UPI ID is selected")
            case _:
                  print("Invalid input")
    case 2 :
            choose = int(input("""Select a option from below
1 → Credit Card
2 → Debit Card
=>   """))  
            match choose :
                 case 1:
                      print("Credit card is selected ")
                 case 2 :
                      print("Debit card is selected")
                 case  _:
                                   print("Invalid input")
    case 3 :
             choose = int(input("""Select a option from below
1 → Add Money
2 → Pay Using Wallet
     =>   """)) 
             match choose :
                 case 1 :
                     print("Add money is selected")
                 case 2:
                     print("Pay using wallet is selected")
                 case _:
                       print("Invalid input")                        
    case _ :
                      print("Invalid input")