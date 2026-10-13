word = input("Enter a string here => ").strip().lower()

flag = True 

for i in word :
    if i == "a" :
        print(" a is Found")
        flag = False
        break
if flag :
    print("a is not found ")          
