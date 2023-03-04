"""
bit string in the bit string is initially n
 bits and every bit is 0
. Then the bit string is changed k
 times. In every change, the bit string is reviewed from left to right. If the bit is 1
, it will become 0
 and the walkthrough continues. If, on the other hand, the bit is 0
, it will become 1
 and the walkthrough ends. What is the bit string like at the end?

You can assume that n
 is in between 1... 20
 and k
 is in between 0... 1000
. In addition, you can assume that: k<2n
 that is, in every change there is at least one bit in the bit string 0
.

Implement a function in the file that returns the final bit string as a string.bitchange.pycreate
"""

def create(n, k):
    # create n number of zeros as list
    bits = [str(0)] * n
    counter = 0
    # traverse through the bits
    for index in range(k):
        # if there
        for j in range(0, index+1):
            if bits[j] == str(1):
                bits[j] = str(0) 
            elif bits[j] == str(0):
                bits[j] = str(1)
                break
        
    return ''.join(bits)
if __name__ == "__main__":
    print(create(5, 0)) # 00000
    print(create(5, 1)) # 10000
    print(create(5, 2)) # 01000
    print(create(5, 3)) # 11000
    print(create(5, 4)) # 00100
    print(create(5, 31)) # 11111
