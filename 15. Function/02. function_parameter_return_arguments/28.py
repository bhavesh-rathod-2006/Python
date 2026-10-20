def convert_temperature(value, scale="C"):
    if scale == "C":
        result = (value * 9 / 5) + 32
    else:
        result = (value - 32) * 5 / 9

    return result


print(convert_temperature(100))
print(convert_temperature(212, "F"))