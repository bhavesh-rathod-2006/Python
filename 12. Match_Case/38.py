topic = int(input("""Select any option from below
1 → Engine
2 → Lights
3 → Music
4 → Navigation
=>   """))


match topic:
    case 1 :
        choose = int(input("""Select a option from below
1 → Start
2 → Stop
=>   """)) 
        match choose :
            case 1 :
                print("Start is selected")
            case 2:
                print("Stop is selected")
            case _:
                  print("Invalid input")
    case 2 :
            choose = int(input("""Select a option from below
1 → Headlights
2 → Indicators
3 → Hazard Lights
=>   """))  
            match choose :
                 case 1:
                      print("Headlights is selected ")
                 case 2 :
                      print("Indicators is selected")
                 case 3:
                      print("Hazard Lights is selected")
                 case  _:
                                   print("Invalid input")
    case 3 :
             choose = int(input("""Select a option from below
1 → Play
2 → Pause
3 → Next
4 → Previous
     =>   """)) 
             match choose :
                 case 1 :
                     print("Play is selected")
                 case 2:
                     print("Pause is selected")
                 case 3:
                     print("Next is selected")
                 case 4:
                       print("Previous is selected")
                 case _:
                       print("Invalid input")
    case 4 :
                 choose = int(input("""Select a option from below
1 → Start Navigation
2 → Stop Navigation
     =>   """))  
                 match choose :
                      case 1:
                           print("Start Navigation is selected ")
                      case 2 :
                           print("Stop Navigation is selected")
                      case  _:
                                        print("Invalid input")                              
    case _ :
                      print("Invalid input")