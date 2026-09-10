hour=int(input("Enter hour "))
if 0<=hour<24:
    minute=int(input("Enter minute "))
    if 0<=minute <59:
        second=int(input("Enter second "))
        if 0<=minute <59:
            print(f"The time is {hour}:{minute}:{second} ")
        else:
            print("second should be greater than 0 and less than 59 ")  
    else:          
        print("minute should be greater than 0 and less than 59 ")  
else:
    print(" hour should be greater than 0 and less than 23 ")        