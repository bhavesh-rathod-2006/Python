name1,name2,name3=input("Enter names of three people ").split()[:3]
age1,age2,age3=map(int,input("Enter theirs ages respectfully ").split()[:3])

if age1==age2==age3 :
    print(f"{name1}, {name2}, {name3} are {age3} years old ")
elif age1==age2!=age3 or age2==age3!=age1 or age3==age1!=age2:
    print(f" two people are at same age  ")  
elif age2>age1<age3:
    print(f"{name1} is youngest person ")    
elif   age1>age2<age3: 
    print(f"{name2} is the youngest person ")  
else:
    print(f"{name3} is the youngest person ")    

