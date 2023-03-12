#!/usr/bin/env python3

import sys

def file_count(filename):
    """
     The function should read the file, count the number of lines, words, and characters in the file, and return a triple with these count in this order. 
     You get division into words by splitting at whitespace. You don't have to remove punctuation.
    """
    with open(filename, 'r') as data:
        datas = data.read()
    
    number_lines = len(datas.split('\n')) - 1
    number_words = len(datas.split())
    number_characters = len([*datas])
    

    # words
    # characters 
    return(number_lines, number_words, number_characters)

def main():
    #filename = "test.txt"
    for filename in sys.argv[1:]:
        lines, words, characters = file_count(filename)
        print(f"{lines}\t{words}\t{characters}\t{filename}")
    
if __name__ == "__main__":
    main()
