
def count(numbers):
    """
    count number difference in 1 interval
    The time complexity will be O(nlogn) because we use sort method
    """

    numbers.sort()

    count_interval = 1
    max_count = 1
    # 13, 14, 15, 15, 16

    #[15, 14, 9, 7, 10, 8]
    #7,8,9,10,14,15
    for index in range (1, len(numbers)):
        prev_number = numbers[index - 1]
        if prev_number + 1 == numbers[index]:

            count_interval += 1

        elif prev_number != numbers[index]:
            max_count = max(max_count, count_interval)
            count_interval = 1

    max_count = max(max_count, count_interval)
    return max_count

if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3
    print(count([14, 15, 16, 15, 13]))# 4
    print(count([15, 14, 9, 7, 10, 8])) #4

"""
The task can be solved effectively with the help of organization in time O(n.logn).

The next solution will first organize the list, and then go through it from left to right. 
The variable contains information on how many different numbers from the list have been extracted up to the current point. 
In turn, the variable has the best result found.

Note that the same number may appear multiple times in the list. 
This should be taken into account in the code so that the repetition of the same number does not clutter up the calculation.countbest

def count(t):
    n = len(t)
    t.sort()
    best = 1
    count = 1
    for i in range(1,n):
        # compare current and previous some if current is not equal to previous + 1
        # re-initialize the count
        if t[i] > t[i-1]+1:
            count = 1
        elif t[i] == t[i-1]+1:
        # if previous and current difference is 1 start counting
            count += 1
        # get the maximum count of number difference by 1
        best = max(best, count)
    return best
"""