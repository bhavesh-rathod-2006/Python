
arr = [ 1 , -45 ,  2, 3 , 38 , 214 , 907 , -18 , -75, 578 ]

for i in arr :
    if i<0 :
        continue
    if i%4==0 and i%6==0 :
        print("Found !!")
        break
else:
    print("No Matching number Found !!")    