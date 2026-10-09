choise = int(input("""select a number of below
1 → Low
2 → Medium
3 → High
4 → Critical
==> """))



match choise:
    case 1 | 2 :
        print("Normal priority ")
    case 3 | 4 :
        print("Urgent Priority ")
    case _ :
        print("Invalid input ")