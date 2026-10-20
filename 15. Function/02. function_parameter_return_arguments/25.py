def calculate_pay(hours, rate=200, bonus=0):
    total = hours * rate + bonus
    return total


print(calculate_pay(8))
print(calculate_pay(8, 300))
print(calculate_pay(8, bonus=500))
print(calculate_pay(hours=8, rate=300, bonus=500))