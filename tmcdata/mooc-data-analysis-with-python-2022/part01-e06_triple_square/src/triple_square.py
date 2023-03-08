#!/usr/bin/env python3

def triple(n):
    return n * 3
def square(n):
    return n ** 2
def main():
    n = 10
    for number in range(1, n+1):
        triple_number, square_number = triple(number), square(number)

        if square_number > triple_number:
            break 
        else:
            print(f"triple({number})=={triple_number} square({number})=={square_number}")
if __name__ == "__main__":
    main()
