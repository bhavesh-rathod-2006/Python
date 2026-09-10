number=int(input("Enter a number "))

if number%5==0 and number%11==0:
    print(f"{number} is divisible by both 3 and 7 ")
elif number%5==0 :
    print(f"{number} is divisible by 3")
elif number%11==0:
    print(f"{number} is divisible by 7")    
else:
    print(f"{number} is divisible by niether 3 nor 7") 