num = int(input("Enter a number => "))

while num%3!=0 or num%5==0:
    print("Not accepted")
    num = int(input("Enter a number => "))

print("Accepted !!")
