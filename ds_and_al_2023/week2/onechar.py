"""
Your task is to calculate in how many substrings of a string each character is the same. For example, in a string, such substrings areabbbcaa
a (thrice)
aa
b (thrice)
bb (twice)
bbb
c
i.e. total 11 part of the queue.

1. Identify all possible substrings of the given string.
2. For each substring, check if all the characters in it are the same.
3. If all characters are the same, count that substring.
4. Return the total count of such substrings.

Time Complexity: O(n)

A bit explaination of this formula:
(similar_char_length*(similar_char_length+1))//2

So, if we add up the number of possible substrings for each starting position, 
we get the total number of substrings that can be formed from the streak. 
This can be expressed as:
k + (k-1) + (k-2) + ... + 3 + 2 + 1
This is just the sum of the integers from 1 to k.
1 + 2 + 3 + ... + n = (n * (n+1)) / 2


"""

def count(s):
    total_char_length = 0
    similar_char_length = 0
    prev_char = ""

    for current_char in s:
        if current_char == prev_char:
            # count all similar character from the string
            similar_char_length += 1
        else:
            # count all the possible similar character sub string length 
            total_char_length += (similar_char_length*(similar_char_length+1))//2

            # re-initialize similar chacter from 1 because we found a new unique character
            similar_char_length = 1
            
            # initialize previous character 
            prev_char = current_char

    # collect the remaining similar character length
    total_char_length += (similar_char_length*(similar_char_length+1))//2
    return total_char_length

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5


"""
Better solution

The idea of the solution is to go through the string from left to right and calculate at each point how many substrings ending in that point are made up of only one character.

This can be done effectively by maintaining a counter that remembers how many characters in a row have been the same. The counter resets when there are two different characters in a string in a row.

The resulting algorithm takes time O(n)
.
def count(s):
    result = 0
    for i in range(len(s)):
        if i == 0 or s[i-1] != s[i]:
            counter = 0
        counter += 1
        result += counter
    return result
"""