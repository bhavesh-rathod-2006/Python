    
operation=input("enter a opration name you want to work on like addition , subtracttion , division , multiplication ")
if operation=="addition" or operation=="subtraction" or operation=="division" or operation=="multiplication" :
    a, b=map(int, input(" enter two numbers").split()[:2])

    if operation=="addition":
        print(f"addition of {a} and {b} is {a+b}")
    elif operation=="subtraction":
        print(f"subtraction of {a} and {b} is {a-b}")
    elif operation=="division" :
        print(f"the division of{a} and {b} is {a/b}")
    elif operation=="multiplication":
        print(f"the multiplication of {a} and {b} is {a*b}")
else:
    print("please enter valid details and try again!!")