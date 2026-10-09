subject = int(input("""Select a option from below
1 → Employee
2 → Manager
=>   """))


match subject:
    case 1 :
        choose = int(input("""Select a option from below
1 → View Profile
2 → Apply Leave
3 → View Salary
=>   """)) 
        match choose :
            case 1 :
                print("view profile is selected")
            case 2:
                print("Apply salary is selected")
            case 3:
                print("View salary is selected")
            case _:
                  print("Invalid input")
    case 2 :
            choose = int(input("""Select a option from below
1 → View Profile
2 → Apply Leave
3 → View Salary
=>   """))  
            match choose :
                 case 1:
                      print("View profile  is selected ")
                 case 2 :
                      print("Apply Leave is selected")
                 case 3:
                      print("View Salary is selected")
                 case  _:
                         print("Invalid input")
    case 3 :
             choose = int(input("""Select a option from below
1 → View Team
2 → Approve Leave
3 → View Reports
     =>   """)) 
             match choose :
                 case 1 :
                     print("View team is selected")
                 case 2:
                     print("Approve Leave is selected")
                 case 3:
                     print("View Reports is selected")
                 case _:
                       print("Invalid input")                         
    case _ :
                      print("Invalid input")