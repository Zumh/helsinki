"""
Use Python to implement the insertion organization described in section 3.1.1 of the course book. Measure the execution time of an algorithm when: n=105
 and the feed contains random order of numbers 1,2,... ,n
.

Make sure that after the algorithm runs, the input is indeed in order, but do not include this in the execution time measurement.

In this task, you will automatically get a point when you indicate the results and the code you are using and press the submit button.

Algorithm execution time: s

Solution:
Performing a full swap of the array elements in each inner for loop iteration is not necessary. Instead, we save the value that we want to insert into the sorted subarray in temporary storage. In place of performing a full swap, we simply copy elements to the right. The saved value can then be inserted into its proper position once that has been located.
from full swap N * 3 
to 
N + 2 
"""
from random import randint 
import time 

n = 10**5
start = time.time()
table = [randint(1, n) for number in range(n)]

for i in range(1, n):
    # store current number from the table
    temp_number = table[i]
    j = i-1
    
    while j >= 0 and table[j] > table[j+1]:
        # copy elements to the right 
        table[j] = table[j-1]
        j -= 1
    # insert current number to correct location
    table[j] = temp_number
    

end = time.time()
print("time elapsed", end-start, "s")