pin = 2468
enter_pin = int(input("Enter PIN => "))
for i in range(3):
    if pin == enter_pin:
        print("Correct PiN")
        break
    if pin != enter_pin:
        print("Incorrect PIN !!")
        enter_pin = int(input("Enter PIN => "))

print("Incorrect pin , Try after 5 min !!")


# There is a bug in this code 
# if user type 
#1234
#1245
#2273
#2468             # correct pin

# But still , compilor execute incorrect pin 

            