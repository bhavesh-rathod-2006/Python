num1 = int(input("Enter first number => "))
num2 = int(input("Enter second number => "))

choose = input("""Choose one of below operator 
+ , - , * , /  ==>   """)


match choose :
    case "+" :
        print(f" Result = {num1+num2}")
    case "-":
        print(f"Result => {num1 - num2}")
    case "*" :
        print(f"Result => {num1*num2}")
    case "/" :
        print(f"Result => {num1/num2}")
    case _:
        print("invalid input ")











































