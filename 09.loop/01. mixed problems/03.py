word=input("Eter any word : ").lower()

score1=0

score2=0

score3=0

score4=0
for i in word:
    if chr(97)==i or chr(101)==i or chr(105)==i or chr(111)==i :
     score1+=2
    elif chr(97)<=i<=chr(122) :
       score2+=1
    if chr(48)<=i<=chr(57):
       score3+=3
    if chr(32)<=i<=chr(47) or chr(59)<=i<=chr(64) or chr(92)<=i<=chr(96) or chr(123)>=i>=chr(126):
          score4+=4
result=score1+score2+score3+score4
print(f"the total score is {score1} + {score2} + {score3} + {score4} ==> {result}")          
    