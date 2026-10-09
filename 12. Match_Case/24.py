status = int(input("""  Chose any one from menu 
1 → Start Exam
2 → View Result
3 → Exit
==> """))


match status :
    case 1 :
         age = int(input("Enter your age => "))
         if age >= 18 :
              print("You can start exam ")
    case 2 :
          print("If you attempt the exam than you can visit your result ")  
    case 3 :
          print("Exiting the portal ")
    case _:
          print("Invalid")         













