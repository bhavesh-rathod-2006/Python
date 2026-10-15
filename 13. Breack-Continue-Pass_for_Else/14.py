
marks= 50 
bag=""
while marks >0 :
    marks=int(input("Enter your marks => "))
    if marks<40 :
        continue
    bag += str(marks) + "  "
print( "good marks => ", bag)      
    

 