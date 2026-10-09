choise = int(input("""select one of below 
1 → View Profile
2 → View Courses
3 → View Marks
4 → View Attendance
5 → Logout
==> """))

match choise:
    case 1 :
        print("Opening profile ")
    case 2:
        print("Opening course ")
    case 3:
        print("Opening marks ")
    case 4:
        print("Opening attendance ")
    case 5 :
        print("logout ")
    case _ :
        print("Invalid setting ")