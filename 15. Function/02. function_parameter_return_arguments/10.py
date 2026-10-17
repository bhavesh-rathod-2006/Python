def get_min_max(a , b ):
    if a>b:
        return (f"{a} is greater than {b}")
    if b>a:
        return (f"{b} is greater than {a}")
    if a==b :
        return (f"Both are aqual => {a}")


    
print(get_min_max(10,7))    
    