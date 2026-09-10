temperature=int(input("Enter temperature in celsius "))

if temperature<0:
    print("Freezing ")
elif 0<temperature<=15:
    print("Very cold ")    
elif 15<temperature<=25:
    print("cold ")
elif 26<=temperature<=35:
    print("Normal ")
else:
    print("Hot ")           