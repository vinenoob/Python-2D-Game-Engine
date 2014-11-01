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
blueHightlight = (0,0,200)
greenHightlight = (0, 200, 0)
# mehImg = pygame.image.load("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine\Meh.png")
# mehHigh = pygame.image.load("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine\mehHigh.png")
img_dict = {
    "mehImg": pygame.image.load("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine\Meh.png"),
    "mehHigh": pygame.image.load("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine\mehHigh.png")

}
tile_dict = {
    "mehImg": pygame.image.load("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine\Meh.png"),
    "mehHigh": pygame.image.load("C:\Python34\GameEngine\Python-2D-Game-Engine\Python-2D-Game-Engine\mehHigh.png")
}
tile_obj_dict = {}
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
            pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, self.width, self.height])
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
    def __init__(self, x, y, width, height, img, color, highlight_color_or_img, text_color, text):
        """
        :param x-color: see Object
        :param text_color: Color of the text
        :param text: What the button will say
        """
        super().__init__(x, y, width, height, img, color)
        self.text = text
        self.highlight_color = highlight_color_or_img
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
        for thing in w:
            tmplst = []
            for meh in thing:
                if meh.isdigit():
                    tmplst += meh
            background += [tmplst]


def draw_background():
    temp2 = 0
    for row in background:
        temp1 = 0
        for thing in row:
            if thing == "0":
                gameDisplay.blit(img_dict["mehImg"], (temp1 * 32, temp2 * 32))
            if thing == "1":
                gameDisplay.blit(img_dict["mehHigh"], (temp1 * 32, temp2 * 32))
            temp1 += 1
        temp2 += 1





def save_background():
    with open("background.txt", "w+") as w:
        for thing in background:
            w.write(str(thing))
            w.write("\n")
        w.close()


# def tile_objty():
#     tile = "tile"
#     tile_id = "-1"
#     for thing in tile_dict:
#         tile_id = str(int(tile_id)+1)
#         tile_obj_dict[tile+tile_id] = Button(0, 0, 32, 32, tile_dict[thing], None, None, None, None)
#         tile_obj_dict[tile+tile_id].value = tile_id
#     print(img_dict)


def map_editor():
    global display_height, display_width
    derp = True
    display_bar = Object(0, 500, 800, 100, None, green)
    # tile_objty()
    black_tile = Button(0, 1, 32, 32, img_dict["mehImg"], None, None, None, None)
    grey_tile = Button(0, 1, 32, 32, img_dict["mehHigh"], None, None, None, None)
    black_tile.value = "0"
    grey_tile.value = "1"
    tile_obj_dict["mehImg"] = black_tile
    tile_obj_dict["mehHigh"] = grey_tile
    tile_spacing = display_width/(len(img_dict)+1)
    read_background()
    timer = 0
    for tile in img_dict:
            num = 1
            for thing in tile_obj_dict:
                # tile_obj_dict[thing]
                tile_obj_dict[thing].x = tile_spacing * num
                tile_obj_dict[thing].y = 534
                num += 1
    tile_set_id = "1"
    save_btn = Button(750,550,50,50,None,red, black, white, "Save")
    while derp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for row in background:
                    print(row)
                pygame.quit()
                quit()
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        gameDisplay.fill(white)
        draw_background()
        display_bar.draw()
        for thing in tile_obj_dict:
            tile_obj_dict[thing].draw()
            # tile_obj_dict[thing].dist_from_mouse = (mouse[0] - tile_obj_dict[thing].x, mouse[1] - tile_obj_dict[thing].y)
            # print(tile_obj_dict[thing].dist_from_mouse)
            tile_obj_dict[thing].was_clicked = False
            if tile_obj_dict[thing].is_clicked() and timer >= 30:
                tile_set_id = tile_obj_dict[thing].value
                # if tile_obj_dict[thing].was_clicked is True:
                #     tile_obj_dict[thing].was_clicked = False
                #     tile_set_id = ""
                # else:
                #     tile_obj_dict[thing].was_clicked = True
                #     tile_set_id = tile_obj_dict[thing].value
        #hardcoded for now
        if left_mouse_click():
            for num in range(25):
                for num2 in range(18):
                    if num * 32 < mouse[0] < num* 32 + 32:
                        if num2 * 32 < mouse[1] < num2*32 + 32:
                            if tile_set_id != "-1":
                                print(num2, num)
                                background[num2][num] = tile_set_id

        # num1 = 0
        # for row in background:
        #     num2 = 0
        #     for cell in row:
        #         if num1 * 32 < mouse[0] < num1*32 + 32:
        #
        #             if num2 * 32 < mouse[1] < num2*32 + 32:
        #                 print(num1, num2)
        #                 background[num2][num1] = "0"
        #         num2 += 1
        #     num1 += 1
        # print(mouse)
        save_btn.run(smallFont, save_background)
        timer += 1
        pygame.display.update()
        clock.tick(30)

def text_objects(text, font, color):

    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def none():
    pass


def main_menu():
    meh = True
    def broken():
        global meh
        print("this is broken")
    playBtn = Button(325, 250, 150, 75, None, green, greenHightlight, black, "Play")
    mapBtn = Button(175, 366, 450, 75, None, blue, blueHightlight, black, "Map Creator")
    settingsBtn = Button(275, 482, 250, 75, None, black, grey, white, "Settings")
    while meh:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        playBtn.run(mediumFont, none)
        # 2 is not broken. Just have to do editor
        mapBtn.run(mediumFont, none)
        settingsBtn.run(mediumFont, none)
        if playBtn.is_clicked():
            meh = False

        pygame.display.update()
        clock.tick(30)




def game_loop():
    print("filler")
    btn1 = Button(display_width / 2, display_height / 2, 100, 100, None, black, grey, red, "Hello")

    cont = True
    player = Player(100, 100, 32, 32, img_dict["mehImg"], None)
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
        draw_background()

        #Update screen
        pygame.display.update()
        clock.tick(30)

map_editor()
main_menu()
game_loop()