board=[[4,2,4,2],[4,4,8,2],[8,8,8,0],[8,4,4,8]]
fork=board
s=4
def checkrow1_w():
    y=0
    while(y<s):
        for x in range(s-1):

            if(board[x][y]==board[x+1][y]):
                board[x][y]=board[x][y]*2
                board[x+1][y]=0
        y=y+1
def checkrow2_w():
    t=0
    while t<s:
        for x in range(s-1):
            if(board[x][t]==0 and board[x+1][t]!=0 or board[x][t]==0):
                board[x][t]=board[x+1][t]
                board[x+1][t]=0
        t=t+1
def checkrow_w(s):
    checkrow1_w()
    for q in range(s):

        checkrow2_w()
checkrow_w(4)
damn=0
for x in range(4):
    for y in range(4):
        if fork[x][y]==board[x][y]:
            damn=damn+1
if damn!=16:
    print("yeah")
