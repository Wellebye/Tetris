import pygame, random

import pygame, random, sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Variables
startmenu = False

# Load images
but_singleplayer_img = pygame.image.load("but_singleplayer.png").convert_alpha()
but_highscore_img = pygame.image.load("but_highscore.png").convert_alpha()
but_quit_img = pygame.image.load("but_quit.png").convert_alpha()


class colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]


        

class position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class block:
    def __init__(self, id):
        self.id = id
        self.cell = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 5
        self.rotation_state = 0
        self.colors = colors.get_cell_colors()
    
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns
    
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for Position in tiles:
            Position = position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(Position)
    
    def draw(self, screen):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

class Lblock(block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [position(0, 1), position(1, 1), position(2, 1), position(2, 2)],
            1: [position(1, 0), position(1, 1), position(1, 2), position(2, 0)],
            2: [position(0, 0), position(0, 1), position(1, 1), position(1, 2)],
            3: [position(0, 2), position(1, 0), position(1, 1), position(1, 2)],
        }

class Jblock(block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [position(2, 0), position(2, 1), position(0, 1), position(1, 1)],
            1: [position(0, 0), position(1, 0), position(1, 1), position(1, 2)],
            2: [position(0, 1), position(0, 2), position(1, 1), position(2, 1)],
            3: [position(1, 0), position(1, 1), position(1, 2), position(2, 2)],
        }

class Iblock(block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [position(1, 0), position(1, 1), position(1, 2), position(1, 3)],
            1: [position(0, 2), position(1, 2), position(2, 2), position(3, 2)],
            2: [position(2, 0), position(2, 1), position(2, 2), position(2, 3)],
            3: [position(0, 1), position(1, 1), position(2, 1), position(3, 2)],
        }

class Oblock(block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [position(0, 0), position(0, 1), position(1, 0), position(1, 1)],
            1: [position(0, 0), position(0, 1), position(1, 0), position(1, 1)],
            2: [position(0, 0), position(0, 1), position(1, 0), position(1, 1)],
            3: [position(0, 0), position(0, 1), position(1, 0), position(1, 1)],
        }

class Sblock(block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [position(0, 1), position(0, 2), position(1, 0), position(1, 1)],
            1: [position(0, 1), position(1, 1), position(1, 2), position(2, 2)],
            2: [position(1, 1), position(1, 2), position(2, 0), position(2, 1)],
            3: [position(0, 0), position(1, 0), position(1, 1), position(2, 1)],
        }

class Tblock(block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [position(0, 1), position(1, 0), position(1, 1), position(1, 2)],
            1: [position(0, 1), position(1, 1), position(1, 2), position(2, 1)],
            2: [position(1, 0), position(1, 1), position(1, 2), position(2, 1)],
            3: [position(0, 1), position(1, 0), position(1, 1), position(2, 1)],
        }

class Zblock(block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [position(0, 0), position(0, 1), position(1, 1), position(1, 2)],
            1: [position(1, 0), position(1, 1), position(1, 2), position(2, 1)],
            2: [position(1, 0), position(1, 1), position(2, 1), position(2, 2)],
            3: [position(0, 1), position(1, 0), position(1, 1), position(2, 0)],
        }



class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = colors.get_cell_colors()



    def draw(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 1, row * self.cell_size + 1, self.cell_size - 1,
                                        self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        position = pygame.mouse.get_pos()

        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


singleplayer_button = Button(SCREEN_WIDTH/2 - but_singleplayer_img.get_width()/2, SCREEN_HEIGHT/2 - but_singleplayer_img.get_height() - 50, but_singleplayer_img, 1)
highscore_button = Button(SCREEN_WIDTH/2 - but_highscore_img.get_width()/2, SCREEN_HEIGHT/2 - but_highscore_img.get_height()/2, but_highscore_img, 1)
quit_button = Button(SCREEN_WIDTH/2 - but_quit_img.get_width()/2, SCREEN_HEIGHT/2 + but_highscore_img.get_height()/2 + 50, but_quit_img, 1)

clock = pygame.time.Clock()

game_grid = Grid()

block = Jblock()

game_started = False
game_paused = False


run = True
while run:

    screen.fill((202, 228, 255))

    if not game_started:
        if singleplayer_button.draw():
            game_started = True

        if highscore_button.draw():
            pass

        if quit_button.draw():
            run = False

        singleplayer_button.draw()
        highscore_button.draw()
        quit_button.draw()
    else:
        screen.fill((202, 228, 255))
        game_grid.draw()
        block.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("Goodbye World!")


    pygame.display.update()
    clock.tick(60)

pygame.quit()