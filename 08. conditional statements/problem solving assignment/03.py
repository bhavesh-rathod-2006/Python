number1,number2=map(int,input("Enter two numbers ").split()[:2])

if number1>number2:
    print(f"the larger number is {number1} ")
elif number2>number1:
    print(f"the larger number is {number2} ")  
else:
    print("Both are equal ")      

