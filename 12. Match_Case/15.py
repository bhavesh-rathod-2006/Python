choise = int(input("""select a number of below 
1 → Bronze
2 → Silver
3 → Gold
4 → Platinum
==> """))



match choise:
    case 1 | 2 :
        print(" Basic Membership ")
    case 3 | 4 :
        print("Premium Membership")
    case _ :
        print("Invalid input ")