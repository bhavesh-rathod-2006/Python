number1,number2,number3=map(int,input("Enter three numbers ").split()[:3])

if number2>number1<number3:
    print(f"{number1} is smallest number")
elif number1>number2<number3:
    print(f"{number2} is the smallest number ")   
else:
    print(f"{number3} is the smallest number ")     