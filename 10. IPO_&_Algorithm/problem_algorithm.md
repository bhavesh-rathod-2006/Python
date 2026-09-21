## Assignment
___
### Problem 1
Take two numbers and print their sum.

#### IPO

Input 
    
    read 1st number
    read 2nd number

Prosece    
    
    add both number
    store the result

Output

     print the result
    
____

#### Algorithm

1. start
2. take 1st input
3. takes second input
4. add the numbers
5. store the result
6. pritn the result
7. stop

____

#### Dry run with at least two cases

##### Case 1
- support user gives two values like 5 and 7 
- then the program add the numbers and store result
- then print the result 12

 ##### Case 2
 
- support user gives two values like 18 and 4 
- then the program add the numbers and store result
- then print the result 22

____

#### Python code

```bash
number_1=int(input("Enter first number"))  
number_2=int(input("Enter second number"))

total=number_1 + number_2 

print(f"the sum of {number_1} and {number_2} is {total}")

```

