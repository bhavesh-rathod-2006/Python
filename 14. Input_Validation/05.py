password = input("Enter a password =>  ").strip()

while len(password)<8 :
    print("Not accepted !!")
    password = input("ENter a password =>  ").strip()

print("Accepted !!")

