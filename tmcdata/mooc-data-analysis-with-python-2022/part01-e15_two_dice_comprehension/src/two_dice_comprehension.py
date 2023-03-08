#!/usr/bin/env python3

def main():
    target_sum = 5
    number = 6

    for pair in [(column_number, row_number) for column_number in range(1, number+1) for row_number in range(1, number+1) if column_number + row_number == target_sum]:
        print(pair)
if __name__ == "__main__":
    main()

"""
Pythonic way 
print("\n".join(f"({a},{b})" for a in range(1, 7) for b in range(1, 7) if a + b == 5))
"""
