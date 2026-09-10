amount=int(input("Enter purchase amount "))
a=amount*0.2
b=amount*0.15
c=amount*0.1
d=amount*0.05
amount1=amount-a
amount2=amount-b
amount3=amount-c
amount4=amount-d
if amount>=5000:
    print(f" there is 20% discount if purchased amount is greater than equal to 5000 \n the final amount is = {amount1} ")
elif 2000<=amount<=4999: 
     print(f" there is 15% discount if purchased amount is between 2000 to 4999 \n the final amount is = {amount2} ")   
elif 1000<=amount<=1999:
      print(f" there is 10% discount if purchased amount is between 1000 to 1999 \n the final amount is = {amount3} ")
elif 500<=amount<=999:
      print(f" there is 5% discount if purchased amount is between 500 to 999 \n the final amount is = {amount4} ")
else:
      print(f" there is 0% discount if purchased amount is less than 500 \n the final amount is = {amount} ")




