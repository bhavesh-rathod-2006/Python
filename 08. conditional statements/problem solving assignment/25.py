math,python,html,js,cpp=map(int,input("Enter Your marks each").split()[:5])
avg=(math+python+html+js+cpp)/5
if 0<=math<=100 and 0<=python<=100 and 0<=html<=100 and 0<=js<=100 and 0<=cpp<=100:
    if math<35 or python<35 or html<35 or js<35 or cpp<35:
        print("Fail")
    elif avg>=75:
        print("Distinction")
    elif avg>=60:
        print("First Class")
    elif avg>=50:
        print("Second Class")
    elif avg>=35:
        print("Pass")
    else:
        print("Fail")
else:
    print("Your number should be btw 0 to 100")