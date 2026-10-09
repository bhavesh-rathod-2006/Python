bank = int(input("""Select a your  banking status 
1 → Personal Banking
2 → Business Banking
=>   """))

match bank:
    case 1 :
        choise = int(input("""Select a option from below 
1 → Balance
2 → Transfer
3 → Loan
=>   """))
        match choise:
            case 1 :
                print("we Checking your balance ")
            case 2:
                print("We are transfering the ammout ")
            case 3:
                print("We are looking for loan ")
            case _:
                print("Invalid input")

    case 2 :
             choise1 = int(input("""Select a option from below 
1 → Balance
2 → Payroll
3 → Business Loan
=>   """))
             match choise1 :
               case 1 :
                     print("we Checking your balance")
               case 2:
                       print("Payroll ")
               case 3 :
                       print("We are looking for business loan")
               case _:
                       print("Invalid input")
    case _:
          print("Invalid input ")
                       
                       
          

