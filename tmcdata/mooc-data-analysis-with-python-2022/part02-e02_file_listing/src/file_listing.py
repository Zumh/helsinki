#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    pattern = r'.*(\b\d+\b)\s+(\b[a-zA-Z]+\b)\s+(\d{1,2})\s+(\d+):(\d+)\s+(.*)'
    result = []
    # -rwxr-xr-x 1 jttoivon hyad-all    2356 Dec 11 11:50 add_colab_link.py
    with open(filename, "r") as myfile:
        for line in myfile:
            file_size, month, day, hour, minutes, file_name = re.search(pattern, line).groups()
            result.append((int(file_size), month, int(day), int(hour), int(minutes), file_name))
    return result

def main():
    # access rights, number of references, owner's name, name of owning group, file size, date, filename
    # hese fields are separated with one or more spaces. Note that there may be spaces also within these seven fields.
    # (25399, "Nov", 2, 21, 25, "exception_hierarchy.pdf")
    result = file_listing()
    print(result)
if __name__ == "__main__":
    main()

"""
More precise regex and model solution 
 
def file_listing(filename="src/listing.txt"):
    with open(filename) as f:
        lines = f.readlines()
    result=[]
    for line in lines:
        pattern = r".{10}\s+\d+\s+.+\s+.+\s+(\d+)\s+(...)\s+(\d+)\s+(\d\d):(\d\d)\s+(.+)"
        if True:      # Two alternative ways of doing the same thing
            m = re.match(pattern, line)
        else:
            compiled_pattern = re.compile(pattern)
            m = compiled_pattern.match(line)
        if m:
            t = m.groups()
            result.append((int(t[0]), t[1], int(t[2]), int(t[3]), int(t[4]), t[5]))
        else:
            print(line)
    return result
"""