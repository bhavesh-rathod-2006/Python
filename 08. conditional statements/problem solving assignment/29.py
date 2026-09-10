number1,number2,number3=map(int,input("Enter three numbers ").split()[:3])
if number1==number2==number3:
    print("all the numbers are same ")
elif number1==number2!=number3 or number1!=number2==number3 or number1==number3!=number2:
    print(" two numbers are same ")
elif number1<number2<number3:
    print(f"{number2} is second largest number ")    
elif number2<number3<number1:
    print(f"{number3} is second largest number ")    
elif number1<number3<number2:
    print(f"{number3} is second largest number ")
elif number3<number1<number2    :
    print(f"{number1} is second largest number ")
elif number3<number2<number1 :
    print(f" {number2} is second largest number ")   
elif number2<number1<number3  :
    print(f"{number1} is second largest number ")  

       












