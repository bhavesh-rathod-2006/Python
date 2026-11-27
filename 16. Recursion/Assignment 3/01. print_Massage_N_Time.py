

# Write a recursive function that accepts a message and a positive integer n. Print the message exactly n times.

# Example:

# Input: message = "Hello", n = 3


massage = input("Enter a massage => ")
n = int(input("Enter a +ve integer here => "))

def greet(n="1",message = "Hello"):
    if n==0 :
        return
    n -= 1
    greet(n,massage)
    print(massage)

greet(n , massage)