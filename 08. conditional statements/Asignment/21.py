age=int(input("Enter your age "))

if age>=18:
    marks=int(input("Enter your marks "))
    if marks>=40:
        print("You are eligible for final exam")   
    else:
        print("You are not eligible ")    
else:
    print("you are minor , so that you are not eligible")       
