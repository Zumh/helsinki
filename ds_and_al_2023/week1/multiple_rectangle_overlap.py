def rectangle_area(rect):
    # Calculate the area of a rectangle given its coordinates
    return (rect[2] - rect[0]) * (rect[1] - rect[3])

def rectangle_overlap(rect1, rect2):
    # Calculate the overlap area between two rectangles
    x_overlap = max(0, min(rect1[2], rect2[2]) - max(rect1[0], rect2[0]))
    y_overlap = max(0, min(rect1[1], rect2[1]) - max(rect1[3], rect2[3]))
    return x_overlap * y_overlap

def triple_overlap_area(rectangles):
    # Calculate the triple overlap area of a list of rectangles
    if len(rectangles) < 3:
        return 0
    
    x_overlap = max(rect[0] for rect in rectangles) - min(rect[2] for rect in rectangles)
    y_overlap = max(rect[3] for rect in rectangles) - min(rect[1] for rect in rectangles)
    return x_overlap * y_overlap

def total_area(rectangles):
    # Calculate the total area of a list of rectangles
    total_area = sum(rectangle_area(rect) for rect in rectangles)
    
    # Calculate the overlap area between each pair of rectangles
    overlap_area = 0
    for i in range(len(rectangles)):
        for j in range(i+1, len(rectangles)):
            overlap_area += rectangle_overlap(rectangles[i], rectangles[j])
    
    # Calculate the triple overlap area of the rectangles
    triple_overlap = triple_overlap_area(rectangles)
    
    # Return the area covered by at least one of the rectangles
    return total_area - overlap_area + triple_overlap
if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(total_area([rec1,rec2,rec3])) # 16
