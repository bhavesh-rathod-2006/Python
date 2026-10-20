def format_name(first , last , uppercse = False):
    for i in first :
        if i in first.upper():
            first = first.upper()
            last = last.upper() 
            return first + " " + last 

    for j in last :
        if j in last.upper():
              first = first.upper()
              last = last.upper() 
              return first + " " + last


print(format_name("bhavesh" , "Rathod"))