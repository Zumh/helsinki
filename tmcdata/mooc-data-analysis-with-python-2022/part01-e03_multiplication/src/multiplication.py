#!/usr/bin/env python3

def main():
    # Enter your solution here
    n = 10
    number = 4
    for each_number in range(n+1):
        product = number * each_number
        print(f"{number} multiplied by {each_number} is {product}")
if __name__ == "__main__":
    main()
