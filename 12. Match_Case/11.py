choise = int(input("""select one of below 
1 → pdf
2 → jpg
3 → png
4 → mp3
5 → mp4
==> """))



match choise:
    case 1 :
        print("Document selected  ")
    case 2:
        print("Image selected ")
    case 3:
        print("Image selected")
    case 4:
        print("Audio selected ")
    case 5:
            print("Video selected ")
    case _ :
        print("Unknown File Type ")