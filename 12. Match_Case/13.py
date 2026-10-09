choise = int(input("""select a number of day 
1 → Monday
2 → Tuesday
3 → Wednesday
4 → Thursday
5 → Friday
6 → Saturday
7 → Sunday
==> """))



match choise:
    case 1 | 2 | 3| 4| 5 :
        print("Weekday ")
    case 6 | 7 :
        print("Weekend  ")
    case _ :
        print("Invalid Day ")