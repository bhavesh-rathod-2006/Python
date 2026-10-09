choise = int(input("""select one of below 
1 → admin
2 → teacher
3 → student
4 → guest
==> """))



match choise:
    case 1 :
        print("Full access ")
    case 2:
        print("Teacher Dashboard ")
    case 3:
        print("Student Dashboard")
    case 4:
        print("Limited Access ")
    case _ :
        print("Invalid Role ")