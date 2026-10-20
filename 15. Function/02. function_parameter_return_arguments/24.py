def apply_discount(price, discount=0):
    amount = price * discount / 100
    final_price = price - amount

    return final_price


print(apply_discount(1000, 20))
print(apply_discount(1000))