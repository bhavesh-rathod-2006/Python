ticket = int(input("""Select a movie ticket 
1 → Regular
2 → Premium
3 → VIP
=>   """))


match ticket :
    case 1 :
        age = int(input("Enter your age => "))
        if age<5 :
            print("Free Entry")
        else :
            print("Ticket type => Regular  ")    
    case 2 :
            age = int(input("Enter your age => "))
            if age<5 :
                print("Free Entry")
            else :
                print("Ticket type => Premium  ")   
    case 3 :
            age = int(input("Enter your age => "))
            if age<5 :
                print("Free Entry")
            else :
                print("Ticket type => VIP ")  
    case _:
          print("Invalid choise ")
                            
