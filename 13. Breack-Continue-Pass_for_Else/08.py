

word = input("Enter a word here ==> ")

flag = True 

for i in range(0,len(word)):
    if i == "a" :
        print("a is Found ")
        flag = False 
        break

if flag :
    print(" a is not Found ")
    


