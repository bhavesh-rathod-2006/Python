number1=int(input("Enter first number number "))
number2=int(input("Enter second number number "))
operator=(input("""Enter a sign of operator (+ , - , * , / )   """)).strip()[:1]

if operator=="+" or operator=="_" or operator=="*" or operator=="/" :
    if operator=="+" :
        print(number1+number2, "is the result ")
    elif operator=="-"  :
        print(number1-number2,"is the result ")
    elif operator=="*":
        print(number1*number2,"is the result ")
    else:
        if number2==0:
            print("you can't divide by zero ")    
        else:
            print(a/b,"is the result ")     
else:
    print("you can only use this (+ , - , * , / ) signs ")             