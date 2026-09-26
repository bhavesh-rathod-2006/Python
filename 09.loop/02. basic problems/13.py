
# METHOD 1

# for i in range(1,10,2):
#     for j in range(1,i+1,2):
#         print( j, end=" ")
#     print()

# METHOD 2

# for i in range(1,6):
#     a=1
#     for j in range(i):
#         print(a,end=" ")
#         a += 2
#     print()    

# METHOD 3

# for i in range(1,6):
#     for j in range(1,2*i,2):
#         print(j , end=" ")
#     print()
        

#  METHOD 4

number=int(input("Enter a number : "))
for i in range(1,number+1):
    for j in range(1,i+1):
        print(2*j-1,end=" ")
    print()    




































