choise = int(input("""select a number of below
1 → Savings
2 → Current
==> """))



match choise:
    case 1:
        choise1 = int(input("""select a number of below
1 → Check Balance
2 → Deposit
3 → Withdraw
==> """))
        match choise1:
            case 1 :
                print("Saving account => Checking balance ")
            case 2 :
                print("Saving account => Depositing money ")
            case 3 :
                print("Saving account => Withdraw selected ")
            case _:
                print("Invalid input ")
        
    case 2:
        choise2 = int(input("""select a number of below
1 → Check Balance
2 → Deposit
3 → Withdraw
==> """))
        match choise2:
             case 1 :
                 print("Current account => Checking balance ")
             case 2 :
                  print("Current account => Depositing money ")
             case 3 :
                    print("Current account => Withdraw selected ")
             case _:
                  print("Invalid input ")
             
    case _:
                    print("Invalid input ")
