unit = int(input("""  Chose a unit conversation from menu 
1 → Kilometers to Meters
2 → Meters to Kilometers
3 → Kilograms to Grams
4 → Grams to Kilograms
==> """))

num = int(input("Enter a number "))

match unit :
    case 1 :
        print(f"{num*1000} meters")
    case 2 :
        print(f"{num/1000} kilometers")
    case 3 :
        print(f"{num*1000} grams ")
    case 4: 
        print(f"{num/1000} kilogramgs")
    case _:
        print("Invalid input ")
























