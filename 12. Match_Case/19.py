choise = int(input("""select a number of below
1 → Vegetarian
2 → Non-Vegetarian
==> """))



match choise:
    case 1:
        choise1 = int(input("""select a number of below
1 → Paneer
2 → Dal
3 → Veg Biryani
==> """))
        match choise1:
            case 1 :
                print("Paneer  selected")
            case 2 :
                print("Dal selected ")
            case 3 :
                print("Veg Biryani selected ")
            case _:
                print("Invalid input ")
        
    case 2:
        choise2 = int(input("""select a number of below
1 → Chicken Biryani
2 → Chicken Curry
3 → Fish Fry
==> """))
        match choise2:
             case 1 :
                 print("Chicken biryani selected ")
             case 2 :
                  print("Chicken curry selected ")
             case 3 :
                    print("Fish Fry selected ")
             case _:
                  print("Invalid input ")
             
    case _:
                    print("Invalid input ")
