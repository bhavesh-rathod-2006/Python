category = int(input("""Select a category
1 → Starters
2 → Main Course
3 → Desserts
4 → Drinks
=>   """))


match category:
    case 1 :
        choose = int(input("""Select a option from below
1 → Soup
2 → Spring Roll
3 → Garlic Bread
=>   """)) 
        match choose :
            case 1 :
                print("Soup is selected")
            case 2:
                print("Spring roll is selected")
            case 3:
                print("Garlic bread is selected")
            case _:
                  print("Invalid input")
    case 2 :
            choose = int(input("""Select a option from below
1 → Pizza
2 → Pasta
3 → Biryani
=>   """))  
            match choose :
                 case 1:
                      print("Pizza is selected ")
                 case 2 :
                      print("Pasta is selected")
                 case 3:
                      print("Biryani is selected")
                 case  _:
                                   print("Invalid input")
    case 3 :
             choose = int(input("""Select a option from below
  1 → Ice Cream
2 → Cake
3 → Gulab Jamun
     =>   """)) 
             match choose :
                 case 1 :
                     print("Ice cream is selected")
                 case 2:
                     print("Cake is selected")
                 case 3:
                     print("Gulab Jamun is selected")
                 case _:
                       print("Invalid input")
    case 4 :
                 choose = int(input("""Select a option from below
     1 → Coffee
     2 → Tea
     3 → Juice
     =>   """))  
                 match choose :
                      case 1:
                           print("Coffee is selected ")
                      case 2 :
                           print("Tea is selected")
                      case 3:
                           print("Juice is selected")
                      case  _:
                                        print("Invalid input")                              
    case _ :
                      print("Invalid input")