#!/usr/bin/env python3

def merge(L1, L2):
    result = []
    
    L1_number = L2_number = 0
    L1_index = L2_index = 0
    while L1_index < len(L1) and L2_index < len(L2):
        L1_number = L1[L1_index]
        L2_number = L2[L2_index]

        if L1_number < L2_number:
            result.append(L1_number)
            L1_index += 1
        else:
            result.append(L2_number)
            L2_index += 1
        
       
    # get the remaining numbers
    while L1_index < len(L1):
        result.append(L1[L1_index])
        L1_index += 1
    while L2_index < len(L2):
        result.append(L2[L2_index])
        L2_index += 1
        
    return result

def main():
    L1=[5,3,7,1]
    L2=[6,1,7,3,6]
    print(merge(sorted(L1), sorted(L2)))

if __name__ == "__main__":
    main()

"""
# Better solution 
def merge(L1, L2):
    result = []
    i, j = 0, 0
    # i = j = 0 would also work but leads to bad behaviour with mutable types so not recommended.
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    if i < len(L1):
        result.extend(L1[i:])
    else:
        result.extend(L2[j:])
    return result
"""