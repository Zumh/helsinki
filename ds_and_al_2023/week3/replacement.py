"""
 In the context of the merge sort algorithm, the merge function is called recursively to merge smaller sublists, 
 so the overall efficiency of the merge sort algorithm is O(n log n), where n is the number of elements to be sorted.


To check if the left or right subarray is exhausted, we use two separate while loops in the merge function. 
In each loop, we compare the elements at indices left_index and right_index of the left and right subarrays, respectively. 
We then copy the smaller element to the temporary array and increment the respective index variable (left_index or right_index) and the loop counter variable (mid). 
We repeat this process until one of the subarrays is exhausted, then we copy the remaining elements of the other subarray to the temporary array.

Finally, we copy the sorted elements from temporary array back to table in the original order. The merge_sort function returns the sorted table.
"""


from random import randint 
import time 

n = 10**5
start_time = time.time()
table = [randint(1, n) for number in range(n)]

def merge(left, mid, right, end):

    # merge left and right
    temp_size = end - left + 1
    temporary = [0]*(temp_size)
    temp_index = 0

    left_index, right_index = left, right 
    
    # merge the left and right here 
    while left_index <= mid and right_index <= end:

        if table[left_index] < table[right_index]:
            temporary[temp_index] = table[left_index]
            left_index += 1
        else:
            temporary[temp_index] = table[right_index]
            right_index += 1
        temp_index += 1

    
    # check if left subarray is exhausted, if not collect all the left value that left from previous merge 
    while left_index <= mid : 
        temporary[temp_index] = table[left_index]
        temp_index += 1
        left_index += 1
    
    # check if right subarray is exhausted, if not collect all the right value that left from previous merge 
    while right_index <= end: 
        temporary[temp_index] = table[right_index]
        temp_index += 1
        right_index += 1
    
    # re-store all the sorted numbers from temporary back to table
    for index in range(left, end+1):
        table[index] = temporary[index - left]

def merge_sort(start, end):
    if start < end:
        mid = (start + end)//2
    
        # left side
        merge_sort(start, mid)
        
        # right side 
        merge_sort(mid + 1, end)
        
        merge(start, mid, mid+1, end)
merge_sort(0, len(table)-1)

end_time = time.time()
print("time elapsed", end_time-start_time, "s")