transport = int(input("""Select a your transport 
1 → Flight
2 → Train
3 → Bus
=>   """))


match transport:
    case 1 :
        choose = int(input("""Select a option from below
1 → Economy
2 → Business
=>   """)) 
        match choose :
            case 1 :
                print("flight => economy selected")
            case 2:
                print("flight => Business selected")
            case _:
                  print("Invalid input")
    case 2 :
            choose = int(input("""Select a option from below
1 → Sleeper
2 → AC
=>   """))  
            match choose :
                 case 1:
                      print("Train => Sleeper selected ")
                 case 2 :
                      print("Train => AC selected")
                 case  _:
                                   print("Invalid input")
    case 3:
            choose = int(input("""Select a option from below
1 → Ordinary
2 → Volvo
=>   """))  
            match choose :
                 case 1:
                      print("Bus => Ordinary selected ")
                 case 2 :
                      print("Bus => Volvo selected")
                 case  _:
                                   print("Invalid input")
    case _ :
                      print("Invalid input")
                      
