year=int(input("Enter year"))
if year%4==0:
    month=int(input("Enter month"))
    if month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
        date=int(input("Enter date"))
        if 0<date<=31:
            print(f"{date}/{month}/{year}")
        else:
            print("Write a date btw 1 to 31")
    if month==1 or month==4 or month==6 or month==9 or month==11:
        date=int(input("Enter date"))
        if 0<date<=30:
            print(f"{date}/{month}/{year}")
        else:
            print("Write a date btw 1 to 30")
    else:
        date=int(input("Enter date"))
        if 0<date<=29:
            print(f"{date}/{month}/{year}")
        else:
            print("Write a date btw 1 to 29")
else:
        month=int(input("Enter month"))
        if month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
            date=int(input("Enter date"))
            if 0<date<=31:
                print(f"{date}/{month}/{year}")
            else:
                print("Write a date btw 1 to 31")
        if month==1 or month==4 or month==6 or month==9 or month==11:
            date=int(input("Enter date"))
            if 0<date<=30:
                print(f"{date}/{month}/{year}")
            else:
                print("Write a date btw 1 to 30")
        else:
            date=int(input("Enter date"))
            if 0<date<=28:
                print(f"{date}/{month}/{year}")
            else:
                    print("Write a date btw 1 to 28")