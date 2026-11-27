# Write a recursive function that accepts a positive integer and returns the sum of the digits at even positions, counting positions from the rightmost digit as position 1.

# Example:
# Input: 583246
# Output: 12
# (The digits at even positions from the right are 4, 2, and 8.)



num = int(input("Enter a number => "))

p = 1
sum = 0
def sum_of_even(num):
    global p,sum
    digit = num%10
    if p%2 == 0:
        sum += digit
    p+=1
    if num<10:
        return num
    sum_of_even(num//10)
    return sum
print(sum_of_even(num))    
        


    

    