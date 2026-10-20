def count_digits(number):
    count = 0 
    for i in str(number)  :
        count = count + 1
    return("numbers of digits is  => ",count)    

firstResult , secondResult = count_digits(80765)

print(firstResult , secondResult)