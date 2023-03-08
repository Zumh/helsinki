#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    square_root = math.sqrt((b**2) - (4*a*c))
    denominator = 2*a
    positive_result = ((-b)+(square_root))/denominator
    negative_result = ((-b)-(square_root))/denominator

    return (positive_result, negative_result)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))
    # a = int(input())
    # b = int(input())
    # c = int(input())
    # solve_quadratic(a, b, c)
if __name__ == "__main__":
    main()
