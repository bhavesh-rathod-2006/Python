year=int(input("Enet a leap year "))

if year%4!=0:
    print("Please enter a leap year")
elif year%4==0 and year%100==0:
    print(f"year {year} is divisible by 4 and 100 ") 
else:
    print(f"year {year} is divisible by 4 but not by 100 ")       