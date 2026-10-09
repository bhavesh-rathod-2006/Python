choise = int(input("""select a number of below
1 → Electronics
2 → Clothing
==> """))



match choise:
    case 1:
        choise1 = int(input("""select a number of below
1 → Mobile
2 → Laptop
3 → Headphones
==> """))
        match choise1:
            case 1 :
                print("MObile selected")
            case 2 :
                print("Laptop selected ")
            case 3 :
                print("Headphones selected ")
            case _:
                print("Invalid input ")
        
    case 2:
        choise2 = int(input("""select a number of below
1 → Shirt
2 → Jeans
3 → Shoes
==> """))
        match choise2:
             case 1 :
                 print("Shirt selected ")
             case 2 :
                  print("Jeans selected ")
             case 3 :
                    print("Shoes selected ")
             case _:
                  print("Invalid input ")
             
    case _:
                    print("Invalid input ")
