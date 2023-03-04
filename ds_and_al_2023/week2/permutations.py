"""
You will be given two lists A and B, both of which contain the 1... n
 some permutation (i.e. the numbers in both lists 1... n in some order).

Your task is to calculate how many of the numbers 1... n
 Appears earlier on the list A
 than on the list B
. The goal is that the time requirement of the algorithm is O(n)
.

Implement a function in the file that returns the desired result.
Explanation: In the first example, both lists permutations.pycount
def count(a, b):


if __name__ == "__main__":
    print(count([1,2,3], [1,2,3])) # 0
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5A
 and B
 are identical. Therefore, no figure appears earlier on the list A
 as B
. In the second example, the numbers 2
, 3
 and 4
 appearing on the list A
 with an index earlier than the list B
.

time complexity is o(n)
space complexity is o(n)
"""

def count(a, b):
    """
    The goal is to count earlier appearance of number from 1...n of a or b length in a list.
    This mean if number appear in 1...n a list than b list we start counting that character length.
    """
    count_earlier_character = 0
    a_elements = {}
    for number in range(0, len(a)):
        # store all the number from 1...n from a length index position
        # a's element are the key and each index value are value
        a_elements[a[number]] = number

    for b_index in range(0, len(b)):
        # what ever b's lement is the key for a's element from a dictionary 
        # if a index's number is less than b_index start counting the character
        if a_elements[b[b_index]] < b_index:
            count_earlier_character += 1

    return count_earlier_character
if __name__ == "__main__":
    print(count([1,2,3], [1,2,3])) # 0
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5


"""
Solution
The idea of the solution is to first tabulate in the list the information on which index each number appears on the list positionsB
.

After that, it is enough to visit the list A
 once through. For each index, thanks to the list, we can check in a standard time on which index the number of that item appears on the list positionsB
.

The resulting algorithm takes time O(n)
.
def count(a, b):
    n = len(a)
    positions = [0] * (n+1)
    for i in range(n):
        positions[b[i]] = i
    result = 0
    for i in range(n):
        if i < positions[a[i]]:
            result += 1
    return result
"""