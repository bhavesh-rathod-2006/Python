subject = int(input("""Select a option from below
1 → Student
2 → Teacher
3 → Administration
=>   """))


match subject:
    case 1 :
        choose = int(input("""Select a option from below
1 → Profile
2 → Marks
3 → Attendance
4 → Courses
=>   """)) 
        match choose :
            case 1 :
                print(" profile is selected")
            case 2:
                print("marks is selected")
            case 3:
                print("Attendance is selected")
            case 4:
                            print("Courses is selected")
            case _:
                  print("Invalid input")
    case 2 :
            choose = int(input("""Select a option from below
1 → Students
2 → Enter Marks
3 → Attendance
4 → Courses
=>   """))  
            match choose :
                 case 1:
                      print(" Students is selected ")
                 case 2 :
                      print(" Enter Marks is selected")
                 case 3:
                      print("Attendance is selected")
                 case 4:
                          print("Courses is selected")
                 case  _:
                         print("Invalid input")
    case 3 :
             choose = int(input("""Select a option from below
1 → Fees
2 → Admissions
3 → Notices
4 → Departments
     =>   """)) 
             match choose :
                 case 1 :
                     print("Fees is selected")
                 case 2:
                     print("Admissions is selected")
                 case 3:
                     print("Notices is selected")
                 case 3:
                       print("Departments is selected")
                 case _:
                       print("Invalid input")                         
    case _ :
                      print("Invalid input")