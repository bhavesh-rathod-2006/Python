choise = int(input("""select one of below 
1 → Morning Show
2 → Afternoon Show
3 → Evening Show
4 → Night Show
==> """))



match choise:
    case 1 :
        print("Morning Show selected ")
    case 2:
        print("Afternoon Show selected ")
    case 3:
        print("Evening Show selected ")
    case 4:
        print("Night Show selected ")
    case _ :
        print("Invalid setting ")