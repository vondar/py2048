board=[[4,0,0,0],[0,0,8,0],[0,8,8,0],[4,0,16,8]]
s=4
for row in board:
    print(row)
def checkrow1():
    y=0
    while(y<s):
        for x in range(s-1):

            if(board[x][y]==board[x+1][y]):
                board[x][y]=board[x][y]*2
                board[x+1][y]=0
        y=y+1
def checkrow2():
    t=0
    while t<s:
        for x in range(s-1):
            if(board[x][t]==0 and board[x+1][t]!=0 or board[x][t]==0):
                board[x][t]=board[x+1][t]
                board[x+1][t]=0
        t=t+1
def checkrow_w(s):

    for q in range(s):
        checkrow2()
    checkrow1()
    checkrow2()
checkrow_w(4)
for row in board:
    print(row)
