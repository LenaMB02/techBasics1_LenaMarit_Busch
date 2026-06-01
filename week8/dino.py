# importing required library
import pygame

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255,255,255)

# activate the pygame library
pygame.init()

# create the display surface object
# of specific dimension.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
# use convert_alpha() for png images
img = pygame.image.load("dino.png").convert_alpha()

# scale down the dino
img = pygame.transform.scale(img, (100,100))

# option: tint your image if you want
# img.fill((0, 0, 200, 100), special_flags=pygame.BLEND_ADD)

# position of dino
dino_x = 100
dino_y = 100

# Init the clock
clock = pygame.time.Clock()

flag = True
while flag:
    # ticking the clock
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    # moving dino as clock tick
    if dino_x  < SCREEN_WIDTH:
        dino_x += 3
    else:
        dino_x = 0

    # paint the screen with background color
    screen.fill(BACKGROUND_COLOR)
    # Using blit to copy image to screen at a specific location
    screen.blit(img, (dino_x, dino_y))
    # refresh the display
    pygame.display.flip()

pygame.quit()
exit(0)