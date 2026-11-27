# Write a recursive function that accepts a positive integer n and prints all even numbers from 2 up to n.

# Example:

# Input: n = 10
# Output: 2 4 6 8 10


n = int(input("Enter a positive & even intezer => "))


if n>0 and n%2==0 :
    count = 2
    def even_num(n):
        global count
        print(count)
        if count == n :
            return
        count += 2
        even_num(n)
    even_num(n)
else:
    print("input intezer should be even & positive ")


    



