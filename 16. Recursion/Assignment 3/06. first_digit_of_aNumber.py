# Write a recursive function that accepts a non-negative integer and returns its first (leftmost) digit.

# Do not convert the number into a string.

# Example:

# Input: 5837
# Output: 5


num = int(input("Enter a positive number => "))

def first_digit(num):
    digit = num%10
    floor = num//10
    if num < 10 :
        return digit
    return first_digit(floor)

print(first_digit(num))

