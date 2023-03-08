#!/usr/bin/env python3

def sum_equation(L):
   
    return(' + '.join(str(0) if L == [] else map(lambda number:str(number), L)) + " = " + str(sum(L,0)))

def main():
    sum_equation([1,5,7])
    sum_equation([])
if __name__ == "__main__":
    main()
