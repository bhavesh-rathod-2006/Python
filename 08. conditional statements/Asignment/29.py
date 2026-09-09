is_student=input("are you a student , yes or no ").lower().strip()
has_id=input(" do you have the school id yes or no ").lower().strip()
has_ticket=input("do you have the entry ticket , yes or no ").lower().strip()

if is_student=="yes" and has_id=="yes" and has_ticket=="yes":
    print("you can enter in the collage")
else:
    print("you can't enter in the collage ")    