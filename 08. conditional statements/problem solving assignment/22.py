account_balance=int(input("Enter your bank balance "))
withdrawal_amount=int(input("Enter withdrawal amount "))
a=account_balance-withdrawal_amount
if account_balance>0 and withdrawal_amount>0 :
    if withdrawal_amount%100==0 and (account_balance-500)>withdrawal_amount:
        print(f"previous balance={account_balance}\n withdrawal amount = {withdrawal_amount} \n after withdrawal the final balance = {a} ")
    else:
        print("after withdrawal bank balance should be at least 500 rupees \n withdrawal amount should be divisible by the 100 ")    
else:
    print("account balance and withdrawal amount should be greater than 0 ")
