def order_summary(item, quantity=1, price=100, delivery_fee=40):
    total = quantity * price + delivery_fee
    return total


print(order_summary("Book"))
print(order_summary("Book", quantity=2, price=100))
print(order_summary("Book", delivery_fee=10))