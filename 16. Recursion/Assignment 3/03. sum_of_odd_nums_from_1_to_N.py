# Write a recursive function that accepts a positive integer n and returns the sum of all odd numbers from 1 to n.

# Example:

# Input: n = 7
# Output: 16




n = int(input("Enter a positive integer => "))


if n>= 0 :
    count = -1
    def odd_sum(n):
        global count
        count += 2
        if count == n or count == (n-1):
            return count
        return count + odd_sum(n)
    print(odd_sum(n))

else:
    print("input should be positive ")

