def bill(item , quantity = 1 , price = 100 ):
    total = price*quantity
    return (f"{item}'s price is {price} rupees and {quantity} pices are buy , the final total ammount is => {total} ")


print(bill("Pen" , 3 , price = 10 ) )