number=int(input("Enter a whole number "))

if number==0:
    print("The input is zero ")
else:
    if number>0:
        if number%2==0:
            print("the input is possitive and even ")
        else:
            print("the input is possitive and odd ")    
    else:
        if number%2==0:
            print("The input is negative and even ") 
        else:
            print("The input is negative and odd ")     