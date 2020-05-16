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

board=[[0 for a in range(s)]

for b in range(s)]
for row in board:
    print( row)
