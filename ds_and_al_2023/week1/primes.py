"""
following pseudocode presents a function that calculates how many primes are in the range count2... n
.
Implement the function corresponding to the pseudocode with Python. Implement the function into the file in the following body:
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
def count(n):
    total = 0
    for i in range(2, n+1):
        # re-initialize the variable to false before checking the range of prime number
        fail = False

        # check the range of prime between 2 and current number = i - 1
        for j in range(2, i - 1):
            
            # set the flag to True if number is not prime
            # current number check by previous number from 2 to i - 1
            if i % j == 0:
                fail = True
        # if a flag is set to false then the current number is a prime.
        # we count the total amount of prime between 2 - n
        if not fail:
            total += 1
    return total

if __name__ == "__main__":
    print(count(2)) # 1
    print(count(10)) # 4
    print(count(11)) # 5
    print(count(100)) # 25
    print(count(1000)) # 168
