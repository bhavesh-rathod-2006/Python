library = int(input("""Select one of below
1 → Search Book
2 → Issue Book
3 → Return Book
4 → View Issued Books
5 → Exit
=>   """))


match library :
    case 1 :
        print("Searching book ")
    case 2 :
        print("Issuing book ")
    case 3:
        print("Returning book ")
    case 4:
        print("Viewing issued books")
    case 5 :
        print("Exiting ")
    case _:
        print("Invalid input ")
