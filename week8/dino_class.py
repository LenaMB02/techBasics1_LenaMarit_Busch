# importing required library
import pygame

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255,255,255) # RGB

class Dino:
    def __init__(self, pos_x=0, pos_y=100): # default value for start position
        img = pygame.image.load("dino.png")
        self.img = pygame.transform.scale(img, (100,100))
        # init position
        self.pos_x = pos_x
        self.pos_y = pos_y

    def tint(self):
        # option: tint your image if you want
        # self.img.fill((0, 0, 200, 100), special_flags=pygame.BLEND_ADD)
        pass

    def animate(self):
        if self.pos_x < SCREEN_WIDTH:
           self.pos_x += 3
        else:
           self.pos_x = 0

    def draw(self):
        screen.blit(self.img, (self.pos_x, self.pos_y))

# activate the pygame library
pygame.init()

# create the display surface object
# of specific dimension.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the pygame window name
pygame.display.set_caption('image')

# Create one dino object at a start location
dino = Dino(300,0)

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # ticking the clock
    clock.tick(60)

    # update dino's position
    dino.animate()

    # paint the screen with background color
    screen.fill(BACKGROUND_COLOR)
    # Using blit to copy image to screen at a specific location
    dino.draw()
    # refresh the display
    pygame.display.flip()

    # code you need to end pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

pygame.quit()
exit(0)