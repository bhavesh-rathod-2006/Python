color = (input("Choose a color => red, yellow, green ")).lower().strip()


match color:
    case "red" :
        print("Stop")
    case "yellow" :
        print("Wait")
    case "green" :
        print("Go")
    case _ : 
        print("Invalid Signal ")    