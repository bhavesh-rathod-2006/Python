dipartment = int(input("""Select a department  
1 → General Medicine
2 → Cardiology
3 → Orthopedics
4 → Pediatrics
5 → Emergency
=>   """))

match dipartment :
    case 1 :
        print("General Medicine selected ")
    case 2 :
        print("Cardiology selected ")    
    case 3 :
            print("Orthopedics selected ")
    case 4 :
            print("Pediatrics selected ")
    case 5 :
            print("Emergency selected ")
    case _ :
            print("Invalid input")        
