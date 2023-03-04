
def generate(n):

    """
        Find the number at position n in the sequence where:
        every element is the smallest, positive, 
        that has not yet appear in the sequence
        and has one ore more repeating numbers. 
        11,22,33,44,55,66,77,88,99,100,101,110,111,112,113,114
        and n will be less than 1000
    """
    
    # iterate till we encounter n
    term_counter = 0
    nth_number = 11
    while term_counter < n:
        nth_string = str(nth_number)
        unique_number_len = len(set(nth_string))
        nth_number_len = len(nth_string)

        # if unique number length is less than current nth number we found repeated nth number. 
        if unique_number_len < nth_number_len:

            term_counter += 1
            # start counting nth number
            # if nth number and count are the same
            # we found our number that has not yet appear in the sequence
            # positive and repeated number
            if term_counter == n:
                return nth_number

        # if the number is not found yet then keep incrementing
        nth_number += 1
    return nth_number
if __name__ == "__main__":
    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505
