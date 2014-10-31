__author__ = 'jn186953'
import os
import pygame
os.chdir('C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine')
pygame.init()
display_width = 1200
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()
mehImg = pygame.image.load("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine\Meh.png")
mehHigh = pygame.image.load("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine\mehHigh.png")
white = (255, 255, 255)
grey = (100, 100, 100)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
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


class Object():
    def __init__(self, x, y, width, height, img, color):
        """
        :param x: The x coordinate of the object
        :param y: The y coordinate of the object
        :param width: width of the object
        :param height: height of the object
        :param img: If "importing" an import, declare here
        :param color: If just making a square / rect, say color here
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.color = color
        self.center_x = 0
        self.center_y = 0

        def draw(self):
            if self.img is None:
                pygame.draw.rect(gameDisplay, black, [self.x, self.y, self.width, self.height])
            else:
                gameDisplay.blit(self.img, (self.x, self.y))

        def hovered(self):
        mouse = pygame.mouse.get_pos()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            return True
        else:
            return False

def game_loop():
    cont = True
    while cont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        pygame.display.update()
        clock.tick(30)

game_loop()
# createBoard(25, 18, background)
# print(background)
#
# with open("background.txt", "w+") as w:
#     for thing in background:
#         w.write(str(thing))
#         w.write("\n")
#     w.close()

# for num in range(10):
#     templst = ()
#     for meh in range(5):
#         inpt = (input("1-3"), input("1-3"))
#         templst += inpt
#     background += templst