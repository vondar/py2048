w=int(input())
board=[[32,32,64],[64,2,256],[2,2,2]]
def checkwin(w):
    key=0
    for row in board:
        for column in row:
            if column==w:
                print("YOU WON!!!!!!!!!!!")
                return 1
            if column==0:
                key=key+1

    y=0
    while(y<s):
        for x in range(s-1):
            if(board[x][y]==board[x+1][y]):
                key=key+1
        y=y+1
    x=0
    while(x<s):
        for y in range(s-1):
            if(board[x][y]==board[x][y+1]):
                key=key+1
        x=x+1
    if key>0:
        return 0
    else:
        print('YOU LOST SORRY')
        return 1
checkwin(w)
