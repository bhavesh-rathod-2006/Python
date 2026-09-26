number=int(input("Enter a number : "))
for i in range(number,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()    

    # Method-2

number1=int(input("Enter a number : "))
for i in range(number1):
    for j in range(number1-i):
        print("*", end=" ")
    print()    
