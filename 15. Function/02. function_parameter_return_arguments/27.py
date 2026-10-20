def compare(a, b):
    if a > b:
        result = "A is greater"
        difference = a - b
    elif b > a:
        result = "B is greater"
        difference = b - a
    else:
        result = "Equal"
        difference = 0

    return result, difference


print(compare(10, 5))
print(compare(3, 8))
print(compare(5, 5))