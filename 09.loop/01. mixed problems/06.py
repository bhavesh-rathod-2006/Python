numbers=(input("Enter Numbers Here ==> "))

count1=0

count2=0

for i in numbers :
    if int(i) % 2 ==0 :
        count1 += 1
    elif int(i) % 2 == 1 :
        count2 += 1

if count1 > count2 :
    print("Even numer is more than odd number")
elif count2 > count1 :
    print("Odd number is more than even number")    
else:
    print("count of even and odd number is same ")    