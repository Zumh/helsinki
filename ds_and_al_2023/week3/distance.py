"""
Find the maximum distance from numbers that already exists in the numbers list.
If we going to add any number from 1..k find the max distance
number 1...k 

"""
def find(numbers, k):
    # sort the numbers list in ascending order
    numbers.sort()
    
    # initialize maximum distance to 0
    maximum_distance = 0
    
    # iterate over the sorted numbers list and compute maximum distance
    for i in range(len(numbers)-1):
        distance = numbers[i+1] - numbers[i] - 1
        if distance % 2 == 0:
            maximum_distance = max(maximum_distance, distance//2)
        else:
            maximum_distance = max(maximum_distance, (distance+1)//2)
            
    # check if the first or last number can extend the maximum distance
    if numbers[0] != 1:
        maximum_distance = max(maximum_distance, numbers[0]-1)
    if numbers[-1] != k:
        maximum_distance = max(maximum_distance, k-numbers[-1])
        
    return maximum_distance



if __name__ == "__main__":
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843))


"""
def find(t, k):
    t.sort()
    # adds a number to the beginning or end of the range
    result = max(t[0]-1, k-t[-1])
    # a number is added between two numbers
    for i in range(len(t)-1):
        result = max(result, (t[i+1]-t[i])//2)
    return result
"""