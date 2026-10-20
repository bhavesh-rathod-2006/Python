def analyze_number(number):
    if number < 0:
        a = -number
    else:
        a = number

    if number % 2 == 0:
        b = True
    else:
        b = False

    c = len(str(a))

    return a, b, c


print(analyze_number(-123))