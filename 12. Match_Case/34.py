game = int(input("""Select any one of below  
1 → Start Game
2 → Load Game
3 → Settings
4 → Exit
=>   """))


match game :
    case 1 :
        print("Game is starting ")
    case 2 :
        print("Game is loading")
    case 3:
        choose = int(input("""Select any one of below  
1 → Sound
2 → Graphics
3 → Controls
=>   """))
        match choose :
            case 1 :
                print("opening sound setting ")
            case 2:
                print("Opening graphics setting")
            case 3:
                print("Opening the control of setting")
            case _:
                print("Invalid input ")
    case _:
        print("Invalid input")                
            
