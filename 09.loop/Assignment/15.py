number=int(input("Enter a possitive number "))
word=0
for i in range(1,number+1):
    if i%2==0:
        word=word+1
print(word)        