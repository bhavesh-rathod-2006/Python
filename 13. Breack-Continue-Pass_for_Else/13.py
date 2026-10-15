string = input("Enter a word here => ")

character = input(f"Enter a character here that you want to remove from {string} => ")


for i in string :
    if i == character :
        continue
    print(i , end="")
print()    





