# Assignment 4: Generative Art

import random
from turtle import *

# ----------------------------------------------------------------------
# 1. SETUP & CANVAS CONFIGURATION
# ----------------------------------------------------------------------
width = 600
height = 600
setup(width, height)

# Turn off animation for instant drawing, hide cursor
tracer(0, 0)
hideturtle()

# Dark background
bgcolor("#1a1a2e")

# ----------------------------------------------------------------------
# 2. COLOR PALETTE
# A curated modern neon/pastel palette for generative art
# ----------------------------------------------------------------------
color_palette = ["#e94560", "#0f3460", "#16213e", "#533483", "#eebb4d", "#00fff5"]

# ----------------------------------------------------------------------
# 3. GENERATIVE GRID ARTWORK
# Using nested loops, conditionals, and random palette choices
# ----------------------------------------------------------------------
grid_size = 5
step_x = width // grid_size
step_y = height // grid_size

# NESTED LOOP 1: Outer loop for Y-axis (Rows)
for y in range(-height // 2 + step_y // 2, height // 2, step_y):

    # NESTED LOOP 2: Inner loop for X-axis (Columns)
    for x in range(-width // 2 + step_x // 2, width // 2, step_x):

        # Move to the grid position without drawing
        penup()
        goto(x, y)
        pendown()

        # RANDOMNESS + LIST: Pick a random color from the palette list
        chosen_color = random.choice(color_palette)
        color(chosen_color)
        fillcolor(chosen_color)

        # CONDITIONAL STATEMENT: Randomly decide what shape/art to generate
        shape_type = random.choice(["concentric_circles", "star_burst", "filled_square"])

        if shape_type == "concentric_circles":
            # Draw layered shrinking circles
            for radius in range(35, 5, -10):
                penup()
                goto(x, y - radius)  # Offset to keep circle centered
                pendown()
                circle(radius)

        elif shape_type == "star_burst":
            # Draw a rotating star-like line pattern
            num_lines = random.randint(6, 12)
            for _ in range(num_lines):
                penup()
                goto(x, y)
                pendown()
                forward(30)
                backward(30)
                right(360 / num_lines)

        else:  # "filled_square"
            # Draw a rotated filled tile
            begin_fill()
            penup()
            goto(x - 20, y - 20)
            pendown()
            for _ in range(4):
                forward(40)
                left(90)
            end_fill()

# ----------------------------------------------------------------------
# 4. FINAL RENDER
# ----------------------------------------------------------------------
update()  # Render everything from buffer
done()    # Keep window open
