# WRITE YOUR SOLUTION HERE:
"""
Please create an animation where robots fall from the sky randomly. 
When a robot reaches the ground, it starts moving to the left or to the right, and finaly disappears off the screen. 
"""

import pygame
from random import randint

def main():
    pygame.init()
    window_width = 640
    window_height = 480

    window = pygame.display.set_mode((window_width, window_height))
    robot = pygame.image.load("robot.png")
    robots_coordinate = []
    total_robot = 10

    clock = pygame.time.Clock()
    frame_per_second = 60
    speed = 1

    end_window_width = window_width - robot.get_width()
    end_window_height = window_height - robot.get_height()

    for count_robot in range(total_robot):
        x = randint(0,end_window_width)
        y = randint(-10,-1)
        robots_coordinate.append({'x':x, 'y':y})

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit() 


        window.fill((0,0,0))
            
        for robot_coordinate in robots_coordinate:
            window.blit(robot,(robot_coordinate['x'],robot_coordinate['y']))

            # left or right 
            #side = randint(1,-1)
        
        pygame.display.flip()

        for each_robot, robot_coordinate in enumerate(robots_coordinate):
            robot_coordinate['y'] += 1



        clock.tick(frame_per_second)
        
main()