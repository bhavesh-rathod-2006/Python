choise = int(input("""select one of below 
1 → Electronics
2 → Clothing
3 → Books
4 → Grocery
5 → Exit
==> """))

match choise:
    case 1 :
        print("Opening Electronics ")
    case 2:
        print("Opening clothing ")
    case 3:
        print("Opening books ")
    case 4:
        print("Opening grocery ")
    case 5 :
        print("Exiting ")
    case _ :
        print("Invalid setting ")