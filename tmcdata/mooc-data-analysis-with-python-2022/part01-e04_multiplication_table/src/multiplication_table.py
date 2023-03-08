#!/usr/bin/env python3


def main():
    n = 10
    width = 4
    product = ""
    for column_number in range(1, n+1):

        for row_number in range(1, n+1):
            multiplication = column_number * row_number
            # within 4 character width we can print the multiplication or product
            # deafault right align the product
            product += f"{multiplication:4}"
        print(product)
        product = ""

if __name__ == "__main__":
    main()
