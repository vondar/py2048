from os import system, name
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
import copy
print('let us begin!')

s=int(input('enter size of map '))

def check(w):
    p=[]
    key=0


    for i in range(15):
        p.append(2**i)
    for num in p:

        if w==num:
            key=key+1
    return key


while 'true':
    w=int(input('enter winning number '))
    k=check(w)

    if k==0:
        print('error')
    else:
        break
import random
x=random.randint(0,s-1)
y=random.randint(0,s-1)

board=[[0 for a in range(s)]

for b in range(s)]
def display():

    for row in board:
        print( row)

board[x][y]=2
display()

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
    for q in range(s):
        checkrow2_w()
    checkrow1_w()
    checkrow2_w()
def checkrow1_s():
    y=0
    while(y<s):
        for x in range(s-1):

            if(board[x][y]==board[x+1][y]):
                board[x+1][y]=board[x][y]*2
                board[x][y]=0
        y=y+1
def checkrow2_s():
    t=0
    while t<s:
        for x in range(s-1):
            if(board[x+1][t]==0 and board[x][t]!=0 or board[x+1][t]==0):
                board[x+1][t]=board[x][t]
                board[x][t]=0
        t=t+1
def checkrow_s(s):
    for q in range(s):
        checkrow2_s()
    checkrow1_s()
    checkrow2_s()
def checkcolumn1_d():
    x=0
    while(x<s):
        for y in range(s-1):

            if(board[x][y]==board[x][y+1]):
                board[x][y+1]=board[x][y]*2
                board[x][y]=0
        x=x+1
def checkcolumn2_d():
    x=0
    while x<s:
        for y in range(s-1):
            if(board[x][y+1]==0 and board[x][y]!=0 or board[x][y+1]==0):
                board[x][y+1]=board[x][y]
                board[x][y]=0
        x=x+1
def checkcolumn_d(s):
    for q in range(s):
        checkcolumn2_d()
    checkcolumn1_d()
    checkcolumn2_d()
def checkcolumn1_a():
    x=0
    while(x<s):
        for y in range(s-1):

            if(board[x][y]==board[x][y+1]):
                board[x][y]=board[x][y]*2
                board[x][y+1]=0
        x=x+1
def checkcolumn2_a():
    x=0
    while x<s:
        for y in range(s-1):
            if(board[x][y]==0 and board[x][y+1]!=0 or board[x][y]==0):
                board[x][y]=board[x][y+1]
                board[x][y+1]=0
        x=x+1
def checkcolumn_a(s):
    for q in range(s):
        checkcolumn2_a()
    checkcolumn1_a()
    checkcolumn2_a()
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
def addrandom2():


    zero=[]
    def check_zero():

        for x in range(s):
            for y in range(s):
                if board[x][y]==0:
                    zero.append((x,y))
    check_zero()

    rand_coor=random.choice(zero)


    board[int(rand_coor[0])][int(rand_coor[1])]=2
wi=checkwin(w)
if wi==0:
    while('true'):
        key=input()
        if key=='w':
            clear()
            fork=copy.deepcopy(board)
            checkrow_w(s)
            damn=0
            for x in range(s):
                for y in range(s):
                    if fork[x][y]==board[x][y]:
                        damn=damn+1
            if damn==s*s:
                print("wrong boss")
            else:
                addrandom2()
                win=checkwin(w)
                for row in board:
                    print(row)
                if win==1:
                    break
        elif key=='s':
            clear()
            fork=copy.deepcopy(board)
            checkrow_s(s)
            damn=0
            for x in range(s):
                for y in range(s):
                    if fork[x][y]==board[x][y]:
                        damn=damn+1
            if damn==s*s:
                print("wrong boss")
            else:
                addrandom2()
                win=checkwin(w)
                for row in board:
                    print(row)
                if w==1:
                    break
        elif key=='a':
            clear()
            fork=copy.deepcopy(board)
            checkcolumn_a(s)
            damn=0
            for x in range(s):
                for y in range(s):
                    if fork[x][y]==board[x][y]:
                        damn=damn+1
            if damn==s*s:
                print("wrong boss")
            else:
                addrandom2()
                win=checkwin(w)
                for row in board:
                    print(row)
                if win==1:
                    break
        elif key=='d':
            clear()
            fork=copy.deepcopy(board)
            checkcolumn_d(s)
            damn=0
            for x in range(s):
                for y in range(s):
                    if fork[x][y]==board[x][y]:
                        damn=damn+1
            if damn==s*s:
                print("wrong boss")
            else:
                addrandom2()

                win=checkwin(w)
                for row in board:
                    print(row)
                if win==1:
                    break
        else:
            print('invalid input')
