board=[[4,32,64,1024],[4,1024,8,32],[128,8,8,0],[8,4,4,8]]
for row in board:
    print(row)
def checkrow1():
    y=0
    while(y<4):
        for x in range(3):

            if(board[x][y]==board[x+1][y]):
                board[x][y]=board[x][y]*2
                board[x+1][y]=0
        y=y+1
def checkrow2():
    t=0
    while t<4:
        for x in range(3):
            if(board[x][t]==0 and board[x+1][t]!=0 or board[x][t]==0):
                board[x][t]=board[x+1][t]
                board[x+1][t]=0
        t=t+1
def checkrow(s):
    for q in range(s):
        checkrow1()
        checkrow2()
checkrow(4)
for row in board:
    print(row)
