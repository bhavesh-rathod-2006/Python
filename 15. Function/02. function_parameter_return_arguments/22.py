def calculate_stats(a, b, c):
    small = a
    large = a

    if b < small:
        small = b

    if c < small:
        small = c

    if b > large:
        large = b

    if c > large:
        large = c

    total = a + b + c

    return small, large, total


print(calculate_stats(10, 20, 5))