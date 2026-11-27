# Write a recursive function that accepts a non-negative integer number and a digit target. Return True if the target digit appears in the number. Otherwise, return False.

# Do not convert the number into a string.

# Example:

# Input: number = 4826, target = 8
# Output: True




num = int(input("Enter a positive number => "))
target = int(input("Enter your target number => "))
def find_digit(num , target):
    digit = num%10
    floor = num//10
    if target == digit:
        return True
    elif num <10:
        return False
    return find_digit(floor,target)
print(find_digit(num,target))
