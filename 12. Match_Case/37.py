subject = int(input("""Select a option from below
1 → Programming
2 → Mathematics
3 → Communication
=>   """))


match subject:
    case 1 :
        choose = int(input("""Select a option from below
1 → Python
2 → Java
3 → C++
=>   """)) 
        match choose :
            case 1 :
                print("Python is selected")
            case 2:
                print("Java is selected")
            case 3:
                print("C++ is selected")
            case _:
                  print("Invalid input")
    case 2 :
            choose = int(input("""Select a option from below
1 → Algebra
2 → Calculus
3 → Statistics
=>   """))  
            match choose :
                 case 1:
                      print("Algebra is selected ")
                 case 2 :
                      print("Calculus is selected")
                 case 3:
                      print("Statics is selected")
                 case  _:
                                   print("Invalid input")
    case 3 :
             choose = int(input("""Select a option from below
1 → English
2 → Presentation
3 → Interview Skills
     =>   """)) 
             match choose :
                 case 1 :
                     print("English is selected")
                 case 2:
                     print("Presentation is selected")
                 case 3:
                     print("Interview skills is selected")
                 case _:
                       print("Invalid input")                         
    case _ :
                      print("Invalid input")