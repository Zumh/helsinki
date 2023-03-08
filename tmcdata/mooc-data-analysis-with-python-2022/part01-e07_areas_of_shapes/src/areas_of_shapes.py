#!/usr/bin/env python3

import math

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return (base * height)//2

def circle_area(radius):
    return (math.pi * (radius**2))

def main():
    # enter you solution here
      
    shape = ""
    shapes = ['triangle', 'rectangle', 'circle']
    # An endless loop should ask for which shape you want the area be calculated.
    while True:
        shape = input(f"Choose a shape (triangle, rectangle, circle): ")
        # An empty string as input will exit the loop. 
        if shape == "":
            break 
        elif shape not in shapes:
            # If the user gives a string that is none of the given shapes, the message “Unknown shape!” should be printed. 
            print("Unknown shape!")
            # Then it will ask for dimensions for that particular shape.
        else:
            # When all the necessary dimensions are given, it prints the area, and starts the loop all over again.
            if shape == shapes[0]:
                base = int(input("Give base of the triangle: "))
                height = int(input("Give height of the triangle: "))
                area = triangle_area(base, height)
            elif shape == shapes[1]:
                width = int(input("Give width of the rectangle: "))
                height = int(input("Give height of the rectangle: "))
                area = rectangle_area(width, height)

            elif shape == shapes[2]:
                radius = int(input("Give radius of the circle: "))
                area = circle_area(radius) 
            print(f"The area is {area}")
if __name__ == "__main__":
    main()
