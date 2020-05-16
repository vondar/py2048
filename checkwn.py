w=int(input())
board=[[1024,32,64],[64,128,256],[2048,0,0]]
def checkwin(w):
    key=0
    for row in board:
        for column in row:
            if column==w:
                print("YOU WON!!!!!!!!!!!")
                return 1
            if column==0:
                key=key+1
    if key>0:
        return 0
    else:
        print('YOU LOST SORRY')
        return 1
checkwin(w)
