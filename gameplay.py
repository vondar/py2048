board=[[4,0,0,0],[4,0,8,0],[0,8,8,0],[8,0,4,8]]
def checkrow1_w(s):
    y=0
    while(y<s):
        for x in range(s-1):

            if(board[x][y]==board[x+1][y]):
                board[x][y]=board[x][y]*2
                board[x+1][y]=0
        y=y+1
def checkrow2_w(s):
    t=0
    while t<s:
        for x in range(s-1):
            if(board[x][t]==0 and board[x+1][t]!=0 or board[x][t]==0):
                board[x][t]=board[x+1][t]
                board[x+1][t]=0
        t=t+1
def checkrow_w(s):
    checkrow1_w(s)
    for q in range(s):
        checkrow2_w(s)
def checkrow1_s(s):
    y=0
    while(y<s):
        for x in range(s-1):

            if(board[x][y]==board[x+1][y]):
                board[x+1][y]=board[x][y]*2
                board[x][y]=0
        y=y+1
def checkrow2_s(s):
    t=0
    while t<s:
        for x in range(s-1):
            if(board[x+1][t]==0 and board[x][t]!=0 or board[x+1][t]==0):
                board[x+1][t]=board[x][t]
                board[x][t]=0
        t=t+1
def checkrow_s(s):
    checkrow1_s(s)
    for q in range(s):
        checkrow2_s(s)
def checkcolumn1_a(s):
    x=0
    while(x<s):
        for y in range(s-1):

            if(board[x][y]==board[x][y+1]):
                board[x][y]=board[x][y]*2
                board[x][y+1]=0
        x=x+1
def checkcolumn2_a(s):
    x=0
    while x<s:
        for y in range(s-1):
            if(board[x][y+1]==0 and board[x][y]!=0 or board[x][y+1]==0):
                board[x][y+1]=board[x][y]
                board[x][y]=0
        x=x+1
def checkcolumn_a(s):
    checkcolumn1_a(s)
    for q in range(s):
        checkcolumn2_a(s)
def checkcolumn1_d(s):
    x=0
    while(x<s):
        for y in range(s-1):

            if(board[x][y]==board[x][y+1]):
                board[x][y+1]=board[x][y]*2
                board[x][y]=0
        x=x+1
def checkcolumn2_d(s):
    x=0
    while x<s:
        for y in range(s-1):
            if(board[x][y]==0 and board[x][y+1]!=0 or board[x][y]==0):
                board[x][y]=board[x][y+1]
                board[x][y+1]=0
        x=x+1
def checkcolumn_d(s):
    checkcolumn1_d(s)
    for q in range(s):

        checkcolumn2_d(s)
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
for row in board:
    print(row)
while('true'):
    key=input()
    if key=='w':
        checkrow_w(4)

        w=checkwin(32)
        for row in board:
            print(row)
        if w==1:
            break
    elif key=='s':
        checkrow_s(4)

        w=checkwin(32)
        for row in board:
            print(row)
        if w==1:
            break
    elif key=='a':
        checkcolumn_a(4)

        w=checkwin(32)
        for row in board:
            print(row)
        if w==1:
            break
    elif key=='d':
        checkcolumn_d(4)


        w=checkwin(32)
        for row in board:
            print(row)
        if w==1:
            break
    else:
        print('invalid input')
