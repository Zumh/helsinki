# # WRITE YOUR SOLUTION HERE:

import pygame
import cloc 

# initialize pygame object
pygame.init()

robot = pygame.image.load("robot.png")

# set up a window size 
window = pygame.display.set_mode((640,480))

# draw the background color RGB 
window.fill((0,0,0))

# update content 
pygame.display.flip()
# check for event 
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    
    # clock 