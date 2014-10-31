__author__ = 'Jonathan'
import pygame
import os
os.chdir("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine")
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Big Ol' Game")
clock = pygame.time.Clock()
white = (255, 255, 255)
grey = (100, 100, 100)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
mehImg = pygame.image.load("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine\Meh.png")
mehHigh = pygame.image.load("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine\mehHigh.png")
npcID = {"npc1": "unused"}
smallFont = pygame.font.Font("freesansbold.ttf", 12)
mediumFont = pygame.font.Font("freesansbold.ttf", 60)
largeFont = pygame.font.Font("freesansbold.ttf", 115)
background = []


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


    moveAmtX = 0
    moveAmtY = 0
    #Idea for later

    def ret_center_x(self):
        self.center_x = int((self.x + (self.width / 2)))
        return self.center_x

    def ret_center_y(self):
        self.center_y = int((self.y + (self.height / 2)))
        return self.center_y

    def ret_x(self):
        return self.x

    def ret_y(self):
        return self.y

    def ret_height(self):
        return self.height

    def collision(self, obj):
        if self.x + self.width >= obj.x and self.x <= obj.x + obj.width:
            if self.y + self.height >= obj.y and self.y <= obj.y + obj.height:
                return True
        else:
            return False

    def hit_side_right_x(self):
        if self.x + self.width >= display_width:
            return True
        else:
            return False

    def hit_side_left_x(self):
        if self.x <= 0:
            return True
        else:
            return False

    def hit_side_bottom_y(self):
        if self.y + self.height >= display_height:
            return True
        else:
            return False

    def hit_side_top_y(self):
        if self.y <= 0:
            return True
        else:
            return False

    def move(self):
        self.x += self.moveAmtX
        self.y += self.moveAmtY

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

    def stop_screen_hit(self):
        if self.hit_side_top_y() or self.hit_side_bottom_y():
            if self.hit_side_top_y():
                self.y += 1
            if self.hit_side_bottom_y():
                self.y -= 1
            self.moveAmtY = 0
        elif self.hit_side_left_x() or self.hit_side_right_x():
            if self.hit_side_left_x():
                self.x += 1
            if self.hit_side_right_x():
                self.x -= 1
            self.moveAmtX = 0


class Player(Object):
    def check_move(self, event_list):
        for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.moveAmtX = -5
                    elif event.key == pygame.K_d:
                        self.moveAmtX = 5
                    elif event.key == pygame.K_w:
                        self.moveAmtY = -5
                    elif event.key == pygame.K_s:
                        self.moveAmtY = 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.moveAmtX = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        self.moveAmtY = 0



class Button(Object):
    def __init__(self, x, y, width, height, img, color, highlight_color, text_color, text):
        """
        :param x-color: see Object
        :param text_color: Color of the text
        :param text: What the button will say
        """
        super().__init__(x, y, width, height, img, color)
        self.text = text
        self.highlight_color = highlight_color
        self.text_color = text_color

    def run(self, font, action):
        if self.img is not None:
            gameDisplay.blit(self.img, (self.x, self.y))
            if left_mouse_click() and self.hovered():
                action()
        elif self.hovered():
            self.draw_btn(self.highlight_color, font)
            if left_mouse_click():
                action()
        else:
            self.draw_btn(self.color, font)

    def is_clicked(self):
        if left_mouse_click() and self.hovered():
            return True
    def draw_btn(self, color, font):
        pygame.draw.rect(gameDisplay, color, [self.x, self.y, self.width, self.height])
        TextSurf, TextRect = text_objects(self.text, font, self.text_color)
        TextRect.center = (self.x + (self.width / 2), self.y + (self.height / 2))
        gameDisplay.blit(TextSurf, TextRect)

def hello():
    print("Hello!")

def left_mouse_click():
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        return True
    else:
        return False


def read_background():
    global background
    with open("background.txt", "r") as w:
        print("step1")
        for thing in w:
            print(thing)
            tmplst = []
            for meh in thing:
                if meh.isdigit():
                    tmplst += meh
            background += [tmplst]
    print(background)


def draw_background():
    temp2 = 0
    for row in background:
        temp1 = 0
        for thing in row:
            if thing == "0":
                gameDisplay.blit(mehImg, (temp1 * 32, temp2 * 32))
            if thing == "1":
                gameDisplay.blit(mehHigh, (temp1*32, temp2 * 32))
            temp1 += 1
        temp2 += 1


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def game_loop():
<<<<<<< HEAD
    print("filler")
    btn1 = Button(display_width / 2, display_height / 2, 100, 100, None, black, grey, red, "Hello")
    btn2 = Button(320, 0, 320, 320, None, black, grey, red, "Meh")
=======
    btn1 = Button(display_width / 2, display_height / 2, 150, 100, None, black, grey, red, "Hello")
>>>>>>> origin/master
    cont = True
    player = Player(100, 100, 32, 32, mehImg, None)
    read_background()

    while cont:

        event_list = pygame.event.get()
        player.check_move(event_list)
        gameDisplay.fill(white)
        # Don't Draw stuff before this
        player.stop_screen_hit()
        player.move()
        player.draw()
        btn1.run(smallFont, hello)
        btn2.run(smallFont, hello)
        draw_background()

        #Update screen
        pygame.display.update()
        clock.tick(30)


game_loop()