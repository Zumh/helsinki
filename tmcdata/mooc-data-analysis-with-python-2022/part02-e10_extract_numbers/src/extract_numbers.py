#!/usr/bin/env python3

def extract_numbers(s):
    """
    Split the string to words at whitespace using the split() method. 
    Then iterate through each word, and initially try to convert to an int. 
    If unsuccesful, then try to convert to a float. If not a number then skip the word.
    """
    result = []
    for number in s.split():
        try:
            result.append(int(number))
        except:
            try:
                result.append(float(number))
            except:
                pass 


    return result 

def main():
    # [123, 1.2, 13.2, -1]
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
