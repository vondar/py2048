board=[[4,2,4,2],[4,4,8,2],[8,8,8,0],[8,4,4,8]]
# import only system from os
from os import system, name
import pyglet
# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# print out some text
for row in board:
    print(row)

# sleep for 2 seconds after printing output
sleep(2)

# now call function we defined above
clear()
music=pyglet.resource.media('music.mp3')
music.play()
pyglet.app.run()
