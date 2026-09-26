

count_1=0
count_2=0
count_3=0
count_4=0

for i in range(10):
    marks=int(input("Enter marks : "))
    if marks >= 75 :
        print("Excellent")
        count_1=count_1+1
    elif marks>=50:
        print("Good")
        count_2=count_2+1
    elif marks>=35:
        print("Pass")
        count_3=count_3+1
    else:
        print("Fail") 
        count_4=count_4+1       
print(f"the numer of students who  got greater than 74 marks is : {count_1} ")   
print(f"the numer of students who  got marks in range (50 to 74) is : {count_2} ")           
print(f"the numer of students who  got marks in range (35 to 49) is : {count_3} ")    
print(f"the numer of students who  fail in exam  : {count_4} ")    