__author__ = 'jn186953'
import os
os.chdir('C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine')
background = []
num = 1
def createBoard(height, width, background):
    global num
    for number in range(width):
        mehlst = []
        for thing in range(height):
            num *= -1
            if num == 1:
                mehlst += str(0)
            elif num == -1:
                mehlst += str(1)
        background += [mehlst]

createBoard(25, 18, background)
print(background)

with open("background.txt", "w+") as w:
    for thing in background:
        w.write(str(thing))
        w.write("\n")
    w.close()

# for num in range(10):
#     templst = ()
#     for meh in range(5):
#         inpt = (input("1-3"), input("1-3"))
#         templst += inpt
#     background += templst