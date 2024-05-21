import pygame, random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Variables
startmenu = False

# Load images
but_singleplayer_img = pygame.image.load("but_singleplayer.png").convert_alpha()
but_multiplayer_img = pygame.image.load("but_multiplayer.png").convert_alpha()
but_quit_img = pygame.image.load("but_quit.png").convert_alpha()


class block:
    def __init__(self):
        self.x = 5
        self.y = 0
        self.shape = random.choice(["I", "O", "T", "S", "Z", "J", "L"])
        self.rotation = 0

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors()

    def get_cell_colors(self):
        dark_grey = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]

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
multiplayer_button = Button(SCREEN_WIDTH/2 - but_multiplayer_img.get_width()/2, SCREEN_HEIGHT/2 - but_multiplayer_img.get_height()/2, but_multiplayer_img, 1)
quit_button = Button(SCREEN_WIDTH/2 - but_quit_img.get_width()/2, SCREEN_HEIGHT/2 + but_multiplayer_img.get_height()/2 + 50, but_quit_img, 1)

clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

game_started = False
game_paused = False

run = True
while run:

    screen.fill((202, 228, 255))

    if not game_started:
        if singleplayer_button.draw():
            game_started = True

        if multiplayer_button.draw():
            pass

        if quit_button.draw():
            run = False

        singleplayer_button.draw()
        multiplayer_button.draw()
        quit_button.draw()
    else:
        screen.fill((202, 228, 255))
        game_grid.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("Goodbye World!")


    pygame.display.update()
    clock.tick(60)

pygame.quit()
