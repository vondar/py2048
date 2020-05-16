board=[[4,0,0,0],[4,0,8,0],[0,8,8,0],[8,0,4,8]]
for row in board:
    print(row)

def checkcolumn1():
    x=0
    while(x<s):
        for y in range(s-1):

            if(board[x][y]==board[x][y+1]):
                board[x][y+1]=board[x][y]*2
                board[x][y]=0
        x=x+1
def checkcolumn2():
    x=0
    while x<s:
        for y in range(s-1):
            if(board[x][y+1]==0 and board[x][y]!=0 or board[x][y+1]==0):
                board[x][y+1]=board[x][y]
                board[x][y]=0
        x=x+1
def checkcolumn_a(s):
    checkcolumn1()
    for q in range(s):

        checkcolumn2()
checkcolumn_a(4)
for row in board:
    print(row)
