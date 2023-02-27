"""
The following pseudocode presents a recursive function , which checks whether a positive number is checkn
 the power of the runner-up.
Implement the function corresponding to the pseudocode with Python. Implement the function into the file in the following body:
"""

def check(n):
    if n == 1:
        return True

    if n%2 == 0:
        return check(n/2)
    # as soon as we encounter number that is not divisible by 2 we return False
    return False
if __name__ == "__main__":
    print(check(1)) # True

    print(check(8)) # True

    print(check(12)) # False

    print(check(1099511627776)) # True

    print(check(123456789)) # False
