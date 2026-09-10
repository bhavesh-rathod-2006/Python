character=input("Enter a Alphabet ").strip().lower()[:1]
if character=="a" or character=="e"  or character=="i"  or character=="o" or character=="u" :
    print("The character ia a vowel ")
elif character!="a" and character!="e"  and character!="i"  and character!="o" and character!="u" and 'a'<= character <='z':
    print("The character is a consonant ")
else:
    print("The character is invalid ")    


