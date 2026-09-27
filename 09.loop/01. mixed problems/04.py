word=input("Enter a Password : ")

condition1=0

condition2=0

condition3=0

condition4=0



if len(word)>=8 :
       for i in word :
    
        if  chr(65)<=i<=chr(90) :
            condition1+=1
       
               

        if chr(97) <= i <= chr(122) :
            condition2+=1
        
                  

        if chr(48) <= i <= chr(57) :
            condition3+=1
     
            

        if chr(32) <= i <= chr(47) or chr(58) <= i <= chr(64) or chr(91) <= i <= chr(96) or chr(123)>=i>=chr(126) :
            condition4+=1

       if condition1==0  or condition2==0 or condition3==0 or condition4==0 :
          print("There should be at least one uppercase letter , one lowercase letter , one digit and one special character in your password")
       elif condition1>0 and condition2>0 and condition3>0 and condition4>0 :
             if condition1+condition2+condition3+condition4>=16:
               print("Your password is strong ")
             elif condition1+condition2+condition3+condition4>=13: 
                  print(" Your password is Medium ")
             elif condition1+condition2+condition3+condition4>=8 :
                print("Your password is weak")
      


else:
        print("password should be at least 8 characters ")





 
