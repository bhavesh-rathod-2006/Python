choise = int(input("""select a number of below 
1 → Student
2 → Teacher
==> """))



match choise:
    case 1:
        choise1 = int(input("""select a number of below
1 → View courses
2 → View Marks
3 → View Attendance
==> """))
        match choise1:
            case 1 :
                print("Opening student's course ")
            case 2 :
                print("Opening Student's Marks ")
            case 3 :
                print("Opening Student's Attendance ")
            case _:
                print("Invalid input ")
        
    case 2:
        choise2 = int(input("""select a number of below
1 → View Students
2 → Enter Marks
3 → View Attendance
==> """))
        match choise2:
             case 1 :
                  print("Opening student's dashboard ")
             case 2:
                  print("Enter the student's marks ")
             case 3 :
                  print("View the  Attendance ")
             case _:
                  print("Invalid input ")
                   
                  
                  
    case _:
                    print("Invalid input ")
