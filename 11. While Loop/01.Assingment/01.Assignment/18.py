n=int(input("Enter a number "))

i=0

count=0
while i<=n:
    if i%2==1:
        count+=1
    i+=1    

print(f"total sum of even numbers {count}")
