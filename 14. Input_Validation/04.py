choose = int(input("""choose any one option from below
1. View profile
2. Edit profile
3. Settings
4. Exit 
==>   """))

while choose!=1 and choose != 2 and choose != 3 and choose != 4 :
    print("Invalid input !!")
    choose = int(input("""choose any one option from below
1. View profile
2. Edit profile
3. Settings
4. Exit 
==>   """))


print("Valid input !!")    