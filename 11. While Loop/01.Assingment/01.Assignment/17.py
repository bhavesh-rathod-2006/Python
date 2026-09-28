n=int(input("Enter a number "))

i=0
count=0
while i<=n:
    if i%2==0:
        count+=1
    i+=1

print(f"the sum of even numbers is {count}  ")