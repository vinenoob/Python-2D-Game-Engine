__author__ = 'Jonathan'
import pygame

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
mehImg = pygame.image.load("Meh.png")
npcID = {"npc1": "unused"}
smallFont = pygame.font.Font("freesansbold.ttf", 12)
mediumFont = pygame.font.Font("freesansbold.ttf", 60)
largeFont = pygame.font.Font("freesansbold.ttf", 115)


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

    moveAmtX = 0
    moveAmtY = 0

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


class Player(Object):
    pass


class Button(Object):
    def __init__(self, x, y, width, height, img, color, highlight_color, text_color, text):
        super().__init__(x, y, width, height, img, color)
        self.text = text
        self.highlight_color = highlight_color
        self.text_color = text_color

    def run(self, font):
        mouse = pygame.mouse.get_pos()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(gameDisplay, self.highlight_color, [self.x, self.y, self.width, self.height])
            TextSurf, TextRect = text_objects(self.text, font, self.text_color)
            TextRect.center = (self.x + (self.width / 2), self.y + (self.height / 2))
            gameDisplay.blit(TextSurf, TextRect)
        else:
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, self.width, self.height])
            TextSurf, TextRect = text_objects(self.text, font, self.text_color)
            TextRect.center = (self.x + (self.width / 2), self.y + (self.height / 2))
            gameDisplay.blit(TextSurf, TextRect)


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def game_loop():
    print("filler")
    btn1 = Button(display_width / 2, display_height / 2, 100, 100, None, black, grey, red, "Hello")
    cont = True
    player = Player(100, 100, 32, 32, mehImg, None)
    while cont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.moveAmtX = -5
                elif event.key == pygame.K_d:
                    player.moveAmtX = 5
                elif event.key == pygame.K_w:
                    player.moveAmtY = -5
                elif event.key == pygame.K_s:
                    player.moveAmtY = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player.moveAmtX = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player.moveAmtY = 0

        # Don't Draw stuff before this
        gameDisplay.fill(white)
            #Prevent player from hitting sides
        # if player.hit_side_top_y() or player.hit_side_bottom_y():
        #     if player.hit_side_top_y():
        #         player.y += 1
        #     if player.hit_side_bottom_y():
        #         player.y -= 1
        #     player.moveAmtY = 0
        # elif player.hit_side_left_x() or player.hit_side_right_x():
        #     if player.hit_side_left_x():
        #         player.x += 1
        #     if player.hit_side_right_x():
        #         player.x -= 1
        #     player.moveAmtX = 0

        player.move()
        player.draw()
        btn1.run(smallFont)

        #Update screen
        pygame.display.update()
        clock.tick(30)


game_loop()