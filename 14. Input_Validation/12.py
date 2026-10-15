balance = 2000 

deposite_amount = int(input("Enter the value of deposite amount => "))

while deposite_amount<=0 :
    print(f"Cant'n depsite {deposite_amount} ")
    deposite_amount = int(input(" enter a valid amount => "))

new_balance = balance + deposite_amount
print(f"""
=======> Balance Status <=============

Previous amount => {balance}
Deposite amount => {deposite_amount}
New balance => {new_balance} 
""")



