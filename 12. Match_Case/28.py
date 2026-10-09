ticket = int(input("""Select a Railway ticket 
1 → Book Ticket
2 → Cancel Ticket
3 → Check PNR
4 → Train Schedule
5 → Exit
=>   """))




match ticket :
    case 1 :
         print("Ticket is boking ")
    case 2 :
            print("Ticket is cancelling ")
              
    case 3 :
           print("PNR is chacking ")
    case 4 :
            print("Train schedule is opening ")
    case 5 :
            print("Exiting ")        
    case _:
          print("Invalid choise ")
                            














