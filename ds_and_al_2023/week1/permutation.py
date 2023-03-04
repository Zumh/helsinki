"""
Your task is to arrange the numbers 1... n
 so that the sums of all adjacent pairs of numbers are of different sizes. You can give any valid solution.

You can assume that n
 is in between 1... 100th
.

Implement a function in the file that returns a list of numbers permutation.pycreate1... n
, where the sums of all adjacent pairs of numbers are different.
Explanation: In the codebase example
"""
def create(n):
    # generate list of numbers from 1 to n
    lst = list(range(1, n+1))


    # iterate over the list and swap adjacent elements if their sum is equal to the previous sum
    for i in range(1, n):
        if lst[i] + lst[i-1] == lst[i-1] + lst[i-2]:
            lst[i], lst[i-1] = lst[i-1], lst[i]

    return lst
if __name__ == "__main__":

    print(create(6)) # [3, 1, 6, 2, 4, 5]
    print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    print(create(15)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]

"""
Simply sort them in ascending order
def create(n):
    return [i for i in range(1, n+1)]
"""