import random
w=int(input())
x=random.randint(0,w-1)
y=random.randint(1,w-1)

board=[[0 for a in range(w)]

for b in range(w)]
def display():

    for row in board:
        print( row)

board[x][y]=2
display()
