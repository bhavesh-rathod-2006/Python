

# Predict the output: python  
x = 1
def outer():
     x = 2   
     def inner():  
       x = 3        
       print(x)      #  3   
     inner()        
     print(x)    # 2   
outer()   
print(x)  # 1

