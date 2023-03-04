def rectangle_area(rect):
    # Calculate the area of a rectangle given its coordinates
    return (rect[2] - rect[0]) * (rect[1] - rect[3])

def rectangle_overlap(rect1, rect2):
    # Calculate the overlap area between two rectangles
    x_overlap = max(0, min(rect1[2], rect2[2]) - max(rect1[0], rect2[0]))
    y_overlap = max(0, min(rect1[1], rect2[1]) - max(rect1[3], rect2[3]))
    return x_overlap * y_overlap

def triple_overlap_area(rect1, rect2, rect3):
    # Calculate the triple overlap area of three rectangles
    x_overlap = max(0, min(rect1[2], rect2[2], rect3[2]) - max(rect1[0], rect2[0], rect3[0]))
    y_overlap = max(0, min(rect1[1], rect2[1], rect3[1]) - max(rect1[3], rect2[3], rect3[3]))
    return x_overlap * y_overlap

def area(rec1, rec2, rec3):
    # Calculate the total area of the three rectangles
    total_area = rectangle_area(rec1) + rectangle_area(rec2) + rectangle_area(rec3)
    
    # Calculate the overlap area between each pair of rectangles
    overlap_area = 0
    for i in range(3):
        for j in range(i+1, 3):
            overlap_area += rectangle_overlap(eval(f"rec{i+1}"), eval(f"rec{j+1}"))
    
    # Subtract the overlap area of the three rectangles
    triple_overlap = triple_overlap_area(eval("rec1"), eval("rec2"), eval("rec3"))
    
    # Return the area covered by at least one of the rectangles
    return total_area - overlap_area + triple_overlap

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16

"""
To solve this problem, we start by summing up the areas of the given rectangles. However, since the rectangles can overlap, this method may result in an overestimation of the total area.

To address this issue, we need to remove the common area between pairs of rectangles from the total area. We can do this by subtracting the area of the common rectangle between each pair of rectangles.

We can then add back the area of the common rectangle between all three rectangles, which was subtracted twice in the previous step.

It is worth noting that the common area between any two rectangles is always a rectangle (or empty). This means we can simplify the process by adding and subtracting the areas of the rectangles directly.
"""
"""
def area_of(rec):
    width = rec[2]-rec[0]
    height = rec[1]-rec[3]
    return width*height if width > 0 and height > 0 else 0

def intersection(rec1, rec2):
    return (max(rec1[0],rec2[0]),
            min(rec1[1],rec2[1]),
            min(rec1[2],rec2[2]),
            max(rec1[3],rec2[3]))

def area(rec1, rec2, rec3):
    result = area_of(rec1) + area_of(rec2) + area_of(rec3)
    result -= area_of(intersection(rec1,rec2))
    result -= area_of(intersection(rec1,rec3))
    result -= area_of(intersection(rec2,rec3))
    result += area_of(intersection(intersection(rec1,rec2),rec3))
return result
"""