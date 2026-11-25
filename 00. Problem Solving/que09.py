


#  Write a nested function that reads a variable from its enclosing function.

def info():
    name = "Bhavesh"
    def inner():
        nonlocal name
        name += " Rathod"
        print(name)
    inner()
info()    
