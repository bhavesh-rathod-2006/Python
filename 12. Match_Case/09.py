choise = int(input("""select one of below 
1 → Sunny 
2 → Rainy
3 → cloud
4 → snowy
==> """))



match choise:
    case 1 :
        print("Wear sunglasses ")
    case 2:
        print("Carry an umbrella ")
    case 3:
        print("Weather may change")
    case 4:
        print("Wear warm change ")
    case _ :
        print("Invalid setting ")