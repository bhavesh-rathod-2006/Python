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

_____

### Problem 2
Take a number and print whether it is even or odd.

#### IPO

input 
    take a number from user

prosece
    store input in number variable
    if number%2 comes 0 then the number is even 
    otherwise odd

output
    print even or odd

____

#### Algorithm
    
- start
- take a number as input
- store number%2 in result
- if result is 0 then print even
- otherwise print odd

____

#### Dry run with examples

##### example 1

suppoce user give input 7 
program store it and do process 
program cheack 7%2 is 0 or not
if 0 then program prints even
otherwise prints odd


##### example 2

suppoce user give input 16 
program store it and do process 
program cheack 7%2 is 0 or not
if 0 then program prints even
otherwise prints odd


_____
   
#### Python code
```bash
number=int(input("Enter a number"))
if number%2==0:
    print("Even")
else:
    print("Odd")
```
    
____


### Problem 3

Take three numbers and print the largest number.

#### IPO

input 
    read 1st number
    read 2nd number
    read 3rd number

proces
   store all the numbers 
   check which one is largest number
   store the largest

output
    print the result

____

#### Algorithm

- start
- read 1st number
- read 2nd number
- read 3rd number
- check with one is largest number by using comparison operator
- store the largest number
- print the largest number
- stop

_____



#### Dry and run example

##### Example 1
suppose user give the numbers 9 5 2 as a inputs
program do comparison and store the largest number
then is print the largest number and that is 9

##### Example 2
##### Example 1
suppose user give the numbers 8 6 3 as a inputs
program do comparison and store the largest number
then is print the largest number and that is 8

____

```bash
number_1=int(input("Enter the 1st number"))
number_2=int(input("Enter the 2nd number"))
number_3=int(input("Enter the 3rd number"))

if number_2< number_1 > number_3 :
   print(f"the {number_1} is the largest number ")
elif number_1< number_2 > number_3 :
  print(f"the {number_2} is the largest number ")
else :
   print(f"the {number_3} is the largest number ")

```
_____


### Problem 4
Take a person's age and print whether they are eligible to vote. Assume the minimum age is 18.

#### IPO

input
    takes a integer value as a age

procces
    if age is greater than are equal to 18 that means true
    if not that means false

output
   if true than print you are able to vaote
   if false than print you are not able to vote

   
____

#### Algorithm

- start
- take input of age
- check age is greater than 17 or not
- if age is greater than 17 then print able to vote
- otherwise print not able to vote
- stop


____  

#### Dry and run examples

##### Example 1

suppose user gives input 15 as a age
then outputs comes out that you are not able to vote 
and suppose user gives input 19 as a age
then outputs comes out that you are  able to vote 


##### Example 2

suppose user gives input 10 as a age
then outputs comes out that you are not able to vote 
and suppose user gives input 25 as a age
then outputs comes out that you are  able to vote 


____

#### Python code
```bash
age=int(input("Enter your age"))
if age>=18:
  print("You are able to vote")
else:
  print("You are not able to vote")

```

____

### Problem 5
Take the price of an item. Give a 20% discount when the price is greater than or equal to 2000. Print the final price.

#### IPO

input
   take input of price 

proccese
   if the price is greater than 2000 then give 20% discount
   store price*0.2 in a discount variable
   than price-discount in final price
   if the price is less then 2000 
   then store the exact price in final price

   
output
   print the final price

#### Algorithm

- start
- take input of price
- if price is greater than 2000 then give 20% discount
- if less than 2000 than there is no discount
- print the final price
- stop
 
_____

#### Dry and run eaxamples

##### Example 1
suppose user gives input 2500 as a price
the program check the value 
the price is greater than 2000 than program gives discount of 20%
and print price-discount

##### Example 2
suppose user gives input 1500 as a price
the program check the value 
the price is less then 2000 than program store the price as a final price
then print the final price

_____

#### Python code
```bash
price=int(input("Enter the price of product "))
if price>=2000:
   discount=price*0.2
   final_price=price-discount
   print(f"The final price is {final_price} ")
else:
  print(f"The final price is {price}")

```

_____


### Problem 6
Take three subject marks and calculate the average. Print Pass if the average is at least 40; otherwise print Fail.

#### IPO

input
   takes input of marks of three subjects
   
prosece
   store the addition in total
   find the average total/3
   if average is greater than 40 then true
   otherwise false

output
   if condition is true than print pass
   if condition is false than print fail

____

#### Algorithm
- start
- takes marks of three subject
- add then and store in total veriable
- then find average by doing total/3
- if average is greater than 40 then print pass
- otherwise print fail
- stop
   
____

#### Dry and run examples

##### Example 1
suppose the marks are 75 90 and 67
program find the sum of marks first
than find the average of marks
then check the value of average
the average is greater than 40 
the program prints pass as a output.


##### Example 12
suppose the marks are 725 19 and 37
program find the sum of marks first
than find the average of marks
then check the value of average
the average is less than 40 
the program prints fail as a output.

_____

#### Python code
```bash
mark_1=int(input("Enter your html exam marks"))
mark_2=int(input("Enter your css exam marks"))
mark_3=int(input("Enter your python exam marks"))

total=mark-1=mark_2+mark_3
average=total/3

if average>=40:
  print("You are pass")
else:
  print("You are fail")
```

_____
