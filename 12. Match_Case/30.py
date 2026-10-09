food = int(input("""Select a order status 
1 → placed
2 → confirmed
3 → preparing
4 → out_for_delivery
5 → delivered
6 → cancelled
=>   """))


match food :
    case 1:
        print("Your order is placed ")
    case 2:
        print("Your order is confirmed")
    case 3:
        print("Your order is prepared ")
    case 4:
        print("Your order is on the way")
    case 5:
        print("Your order is delivering")
    case 6 :
        print("Your order is cancelling ")
    case _:
        print("Invalid input ")