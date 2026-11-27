# Write a recursive function that accepts a non-negative integer number and a digit target. Return how many times the target digit appears in the number.

# Do not convert the number into a string.

# Example:

# Input: number = 52525, target = 5
# Output: 3


n = int(input("Enter a positive intezer => "))

target = int(input("Enter your target intezer => "))

count = 0
def target_num(n , target):
    global count
    digit = n%10
    floor = n//10
    if digit == target:
        count += 1
    if n <10 :
        return count
    return target_num(floor,target)        

print(target_num(n, target))
