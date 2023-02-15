# WRITE YOUR SOLUTION HERE:

# Please create an animation where ten robots go round in a circle.

import pygame
import math 
def calculate_velocity(robot_distance: int,  end_of_window: int, velocity: int):
    
    if robot_distance == end_of_window:
        velocity = -1
    elif robot_distance == 0:
        velocity = 1
    return velocity

def main():
    # initialize pygame 
    pygame.init() 

    # window dimension
    window_width = 640
    window_height = 480

    # create window for game 
    window = pygame.display.set_mode((window_width, window_height))



    # get the robot image from current directory
    robot = pygame.image.load("robot.png")

    

    # robot dimension
    robot_width = robot.get_width()
    robot_height = robot.get_height()

    robots_coordinate = [{'x':0, 'y':0},
              {'x':0, 'y':0},
              {'x':0, 'y':0},
              {'x':0, 'y':0},
              {'x':0, 'y':0},
              {'x':0, 'y':0},
              {'x':0, 'y':0},
              {'x':0, 'y':0},
              {'x':0, 'y':0},
              {'x':0, 'y':0}]

    # set up clock
    clock = pygame.time.Clock()

    # frame per seconds
    frame_per_seconds = 60

    angle = 0
    speed = 0.01
    # intialize robots 
    for robot_amount, robot in robots_coordinate:
        # Set the initial position and angle of the turtle
        angle = i * 2 * math.pi / N
    # running window time frame
    while True:

        # search for window event that make a window quit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # set up window back ground color with black
        window.fill((0,0,0))
        
        for robot_coordinate in robots_coordinate:
            window.blit(robot, (robot_coordinate['x'],robot_coordinate['y']))

        # update pygame with content 
        pygame.display.flip()
        
        # increment the velocity of robot one
      
        # for robot_number, robot_coordinate in enumerate(robots_coordinate):
        #     robot_number = robot_number + 1
        #     robot_coordinate['x'] = 320+math.cos(angle*(2*math.pi)/robot_number)*100-robot_width/2
        #     robot_coordinate['y']  = 240+math.sin(angle*(math.pi*2)/robot_number)*100-robot_height/2
        
        

        # angle 
        angle += speed

        # make the clock tick for 60 seconds
        clock.tick(frame_per_seconds)

main()


"""
# Import the turtle and math modules
import turtle
import math

# Define the number of robots, the radius and the speed of the circle
N = 10
radius = 200
speed = 0.1

# Create a list of turtles to represent the robots
robots = []
for i in range(N):
    # Create a new turtle
    robot = turtle.Turtle()
    # Set the shape, color and size of the turtle
    robot.shape("turtle")
    robot.color("blue")
    robot.shapesize(2)
    # Set the initial position and angle of the turtle
    angle = i * 2 * math.pi / N
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    robot.penup()
    robot.goto(x, y)
    robot.setheading(angle * 180 / math.pi + 90)
    robot.pendown()
    # Add the turtle to the list
    robots.append(robot)

# Loop until the animation is stopped
while True:
    # Move each robot along the circle
    for i in range(N):
        # Get the current robot
        robot = robots[i]
        # Update the angle by adding the speed
        angle = i * 2 * math.pi / N + speed
        # Calculate the new x and y coordinates of the robot
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        # Move the robot to the new position
        robot.goto(x, y)
        # Set the new heading of the robot
        robot.setheading(angle * 180 / math.pi + 90)
        # Draw a small circle at the new position
        robot.circle(5)
    # Update the speed by adding a small amount
    speed += 0.001
"""