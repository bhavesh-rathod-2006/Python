

#  Create a function that returns another function. Explain which variable remains available and why.

def myFunc():
    name = "Bhavesh"
    def inner():
        nonlocal name 
        name += " Rathod"
        return name
    return inner

counter = myFunc()


print(counter())  # Bhavesh RAthod
print(counter())  # Bhavesh RAthod RAthod
print(counter())  # Bhavesh RAthod RAthod RAthod