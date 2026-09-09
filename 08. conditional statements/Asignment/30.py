age=int(input("Enter your age "))
marks=int(input("Enter your marks "))
has_id=input("if you have id than type yes otherwise no ").lower().strip()


if age>=18 and marks>=40 and has_id=="yes" :
    print("You are eligible ")
else:
    print("You are not eligible ")    