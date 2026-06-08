import pygame
import random
import math
import sys
import os

# No path issues
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()

# Window dimensions
X = 800
Y = 600
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Assignment 8 - Animation')


# --- CLASS DEFINITION ---
class Dino:
    def __init__(self, image_path):
        # 1. Load image (using the convert_alpha method)
        original_image = pygame.image.load(image_path).convert_alpha()

        # Uniqueness requirement: Random scaling for each individual instance
        random_size = random.randint(50, 100)
        self.image = pygame.transform.scale(original_image, (random_size, random_size))

        # 2. Position attribute: MUST be stored in a tuple (x, y)
        start_x = random.randint(100, X - 100)
        start_y = random.randint(100, Y - 100)
        self.position = (start_x, start_y)

        # Random variables for initialization
        self.speed_x = random.choice([-4, -2, 2, 4])
        self.speed_y = random.choice([-4, -2, 2, 4])

        # Bonus requirement: Variables for non-linear movement (circular rotation pattern)
        self.angle = random.uniform(0, 2 * math.pi)
        self.rotation_speed = random.uniform(0.03, 0.08)
        self.radius = random.randint(40, 90)

    # Method 1: move() updates the position on the screen
    def move(self):
        # Tuples in Python are immutable (cannot be directly changed).
        # We unpack it, calculate the movement, and repack it into the tuple.
        curr_x, curr_y = self.position

        # Linear movement
        curr_x += self.speed_x
        curr_y += self.speed_y

        # Screen collision: Bounce back when hitting the window borders
        if curr_x <= 0 or curr_x >= X - self.image.get_width():
            self.speed_x *= -1
        if curr_y <= 0 or curr_y >= Y - self.image.get_height():
            self.speed_y *= -1

        # Non-linear movement adjustment
        self.angle += self.rotation_speed

        # Re-assign the new coordinates back to the tuple
        self.position = (curr_x, curr_y)

    # Method 2: draw() paints the object onto the screen surface
    def draw(self):
        curr_x, curr_y = self.position

        # Calculate the mathematical offset using sine/cosine for the circular rotation effect
        offset_x = math.cos(self.angle) * self.radius
        offset_y = math.sin(self.angle) * self.radius

        # Copy content to screen surface using scrn.blit
        scrn.blit(self.image, (curr_x + offset_x, curr_y + offset_y))


# --- INSTANCES CREATION ---
# Creating a list to hold multiple unique instances of the same class
objects_list = []

# Finding the folder
script_dir = os.path.dirname(os.path.abspath(__file__))
image_absolute_path = os.path.join(script_dir, "roland-garros.png")

for i in range(6):
    # Useing the automatic path variable to load Roland-Garros image flawlessly
    dino_instance = Dino(image_absolute_path)
    objects_list.append(dino_instance)

# --- MAIN GAME LOOP ---
clock = pygame.time.Clock()
status = True

while status:
    # Event iteration over the list of event objects
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

    # 1. Fill the screen background (White colour)
    scrn.fill((255, 255, 255))

    # 2. Iterate through the object list to update position and paint them
    for item in objects_list:
        item.move()  # Triggers position update
        item.draw()  # Triggers surface blit

    # 3. Paint screen one time/update the full display surface
    pygame.display.flip()

    # Cap the framerate at 60 FPS so the animation speed is consistent
    clock.tick(60)

# Deactivate the pygame library and close the program cleanly
pygame.quit()
sys.exit()