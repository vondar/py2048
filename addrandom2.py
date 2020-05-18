import random

board=[[0,2,2] for x in range(3)]
def addrandom2():

    
    zero=[]
    def check_zero():

        for x in range(3):
            for y in range(3):
                if board[x][y]==0:
                    zero.append((x,y))
    check_zero()

    rand_coor=random.choice(zero)


    board[int(rand_coor[0])][int(rand_coor[1])]=2
addrandom2()
for row in board:
    print(row)
