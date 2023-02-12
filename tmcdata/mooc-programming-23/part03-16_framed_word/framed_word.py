"""
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre.
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Sample output
Word: testing

******************************
*          testing           *
******************************
Sample output
Word: python

******************************
*           python           *
******************************
"""

word = input("Word: ")
character = "*"
LENGTH = 30

top_bottom = character * LENGTH
odd_space = ""
word_length = len(word)
if word_length % 2 != 0:
    odd_space = " "

space = " " * ((LENGTH - word_length - 2)//2)
middle = f"{character}{space}{word}{space+odd_space}{character}"
print(f"{top_bottom}\n{middle}\n{top_bottom}")
 