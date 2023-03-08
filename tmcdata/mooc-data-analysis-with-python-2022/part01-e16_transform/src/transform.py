#!/usr/bin/env python3

def transform(s1, s2):
    
    # unpack tuple in the expression area
    result = map(lambda number: int(number[0]) * int(number[1]), zip(s1.split(), s2.split()))
   
    return(list(result))

def main():
    transform("1 5 3", "2 6 -1")

if __name__ == "__main__":
    main()
"""
No lambda but trade off is two map 

def transform(s1, s2):
    return [ a*b for (a, b) in zip(map(int, s1.split()), map(int, s2.split())) ]
"""