choise = int(input("""select one payment method of below 
1 → UPI
2 → Card
3 → cash
4 → wallet
==> """))



match choise:
    case 1 :
        print("UPI Payment method selected  ")
    case 2:
        print("Card Payment method selected ")
    case 3:
        print("Cash Payment method selected")
    case 4:
        print("Wallet Payment method selected ")
    case _ :
        print("Invalid mathod ")