#!/usr/bin/env python3

def detect_ranges(L):
    # assume that no element in the input list appears multiple times.
    sorted_numbers = sorted(L)
    result = []
    start = None 
    for index in range(len(L)):
        current_number = sorted_numbers[index]
        prev_number = sorted_numbers[index - 1]
        
        if index == 0 or current_number != prev_number + 1:
            # start of number or new interval beginning
            start = current_number

        # end of the line or the end of interval
        # don't need to worry about out of rang because we check end of range
        if index == len(L) - 1 or current_number != sorted_numbers[index + 1] - 1:
                end = current_number + 1
                if start == end - 1:
                    # if just one number then append 
                    result.append(start)
                else:
                    result.append((start, end))
   

    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

"""
Model solution with easier way 

def detect_ranges(L):
    if not L:           # empty list
        return L
    L = sorted(L)
#    L.sort()
    result = []
    begin, end = L[0], L[0]
    for x in L:
        if x == end:
            end += 1             # increase range
        else:
            if begin + 1 == end: # range of length 1
                result.append(begin)
            else:
                result.append((begin, end))
            begin = x
            end = begin + 1
    if begin + 1 == end: # range of length 1
        result.append(begin)
    else:
        result.append((begin, end))
    return result
"""
