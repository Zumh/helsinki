# WRITE YOUR SOLUTION HERE:

# Please write a program which draws a hundred robots: ten rows with ten robots in each row.

# WRITE YOUR SOLUTION HERE:

# Please write a program which draws ten robots in a row. The end result should look like this:

import pygame

# initialize s the pygame modules 
pygame.init()

# initialize the windows dimensions
window_x = 640
window_y = 480

# The next one creates a window with the function
# set_mode function takes the window dimensions as a n argument.
window = pygame.display.set_mode((window_x,window_y))

# load image from direct source into variable robot
robot = pygame.image.load("robot.png")

# fill method fills window with colour passed as argument
window.fill((0,0,0))


# get the dimensions of the robot in pixels unit
width = robot.get_width()
height = robot.get_height()

for y in range(10):
    for i in range(10):
        window.blit(robot, (50+50*i, height+y//8))

# x_offset = 0
# y_offset = height
# next_x_offset = width
# amount = 10

# for row in range(amount):
#     x_offset = next_x_offset
#     for column in range(amount):
#         # top right 
#         window.blit(robot,(x_offset, y_offset))

#         x_offset += width
#     y_offset += (height/4)
#     next_x_offset += (width/5)
    


# flip update the window with contents
pygame.display.flip()

while True:
    # return list of event from events collected
    for event in pygame.event.get():

        # Quit event is raise when window exits by clicking
        if event.type == pygame.QUIT:

            # program exit with exit function
            # Ctrl + C can also be use here
            exit()