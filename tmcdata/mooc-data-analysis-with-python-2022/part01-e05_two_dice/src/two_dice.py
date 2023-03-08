#!/usr/bin/env python3

def main():
    target_sum = 5
    number = 6
    for column_number in range(1, number+1):
        for row_number in range(1, number+1):
            current_sum = column_number + row_number
            if current_sum == target_sum:
                print(f"{column_number, row_number}")
if __name__ == "__main__":
    main()
