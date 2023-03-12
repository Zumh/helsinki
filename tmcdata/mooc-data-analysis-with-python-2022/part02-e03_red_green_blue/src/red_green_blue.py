#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result =[]
    with open(filename, 'r') as rgb_files:
        next(rgb_files)
        for content in rgb_files:
            fields = re.findall(r'\d+|[a-zA-Z]+.*', content)
            result.append('\t'.join(fields))
    
    return(result)

def main():
    result = red_green_blue()
    
if __name__ == "__main__":
    main()

"""
Better sollution
def red_green_blue(filename="src/rgb.txt"):
    with open(filename) as in_file:
        l = re.findall(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)\n", in_file.read())
        return [
            "{}\t{}\t{}\t{}".format(r, g, b, name)
            for r, g, b, name
            in l
        ]
"""
