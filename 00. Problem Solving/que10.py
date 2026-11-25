


# Write a function that returns a list. Show that the returned list can be changed by the caller.

def greet():
    name = [ "Hello" , "Hyy" , "Hii" , "Hey"]
    return name
new = greet()
new.append("byy")

print(new)