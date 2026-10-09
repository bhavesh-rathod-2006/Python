choise = int(input("""select one of below 
1 → Check Balance
2 → Withdraw Money
3 → Deposit Money
4 → Change PIN
5 → Exit
==> """))



match choise:
    case 1 :
        print("Check Balance selected ")
    case 2:
        print("Withdraw money selected ")
    case 3:
        print("Deposite money selected ")
    case 4:
        print("Change pin selected ")
    case 5 :
        print("Exit")
    case _ :
        print("Invalid setting ")