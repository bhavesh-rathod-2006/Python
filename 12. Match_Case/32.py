status = int(input("""Select a your status 
1 → Student
2 → Teacher
3 → Parent
=>   """))


match status:
    case 1 :
        choose = int(input("""Select a option from below
1 → Marks
2 → Attendance
3 → Homework
=>   """)) 
        match choose :
            case 1 :
                print("Marks selected")
            case 2:
                print("Attendance selected")
            case 3:
                print("Homework selected")
            case _:
                  print("Invalid input")
    case 2 :
            choose = int(input("""Select a option from below
1 → Enter Marks
2 → Attendance
3 → Assign Homework
=>   """))  
            match choose :
                 case 1:
                      print("Enter marks is selected ")
                 case 2 :
                      print("Attendance is selected")
                 case 3:
                      print("Assign homework is selected")
                 case  _:
                                   print("Invalid input")
    case _ :
                      print("Invalid input")
                      

            
    

         