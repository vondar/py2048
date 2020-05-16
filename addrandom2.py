import random

board=[[0,2,2] for x in range(3)]
for row in board:
    print(row)
zero=[]
def check_zero():

    for x in range(3):
        for y in range(3):
            if board[x][y]==0:
                zero.append((x,y))
check_zero()
for s in zero:
    print(s)
rand_coor=random.choice(zero)
rand_x,rand_y=rand_coor
print(int(rand_x))
board[int(rand_coor[0])][int(rand_coor[1])]=2
for row in board:
    print(row)
