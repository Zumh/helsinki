"""
In The Store Is For Sale n candy, each of which has a certain price. How many candies can you buy at most when you have money x
?

The number of candies is no more than 10^5
, and the price of each candy, and x
 is in between 1...10^9
. The goal is that the time requirement of the algorithm is O(n)
 or O(n logn)
.

Implement a function in the file that indicates how many candies you can buy at most.
Explanation: In the first example, you can buy any two candies. In the second example, you can buy three candies, 
for example, the first three candies on the list, which cost in total candies.pysolve
"""

def solve(prices, x):
    """
    time complexity: O(nlogn)
    """
    count_price = 0
    prices.sort()
    for price in prices:
        if price <= x:
            count_price += 1
            x -= price
        else:
            break 
    return count_price

if __name__ == "__main__":
    print(solve([1, 1, 1, 1], 2)) # 2
    print(solve([2, 5, 3, 2, 8, 7], 10)) # 3
    print(solve([2, 3, 4, 5], 1)) # 0
    print(solve([2, 3, 4, 5], 10**9)) # 4
    print(solve([10**9, 1, 10**9], 10**6)) # 1