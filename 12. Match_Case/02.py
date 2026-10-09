choise = int(input("""select one of below 
1 → Wi-Fi
2 → Bluetooth
3 → Mobile Data
4 → Airplane Mode
5 → Exit
==> """))

match choise:
    case 1 :
        print("wi-fi selected ")
    case 2:
        print("Bluetooth selected ")
    case 3:
        print("Mobile data selected ")
    case 4:
        print("Airplane mode selected ")
    case 5 :
        print("Exit")
    case _ :
        print("Invalid setting ")