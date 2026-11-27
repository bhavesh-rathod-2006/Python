# Write a recursive function that accepts a non-negative integer and returns the product of its digits.

# Example:

# Input: 234
# Output: 24


num = int(input("Enter a positive number => "))

def product_digit(num):
    digit = num%10
    floor = num//10
    if num < 10 :
        return digit
    return digit*product_digit(floor)

print(product_digit(num))