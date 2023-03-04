"""
we use the variables "start" and "end" to keep track of the substring that we're currently looking at. 
We also use the "valid_substring_length" variable to keep track of the number of valid substrings that we've found so far.

The basic idea of the algorithm is as follows:

Initialize "valid_substring_length", "start", and "end" to 0.
Loop through each character in the string:
If the current character is not the prohibited character, 
increment "end" and add the number of valid substrings that can be formed with this new character to "valid_substring_length".
If the current character is the prohibited character, set "start" and "end" to the next character after the current character.
Return "valid_substring_length".

Time Complexity is O(n)
"""
def count(s, c):
   
    start = 0
    end = 0
    valid_substring_length = 0
    for index, letter in enumerate(s):

        if letter != c:
            # if current letter is not prohibited character start counting the end length
            end += 1
            # we imeddiately calculate possible substring length because so many possible formed from this same character.
            valid_substring_length += end - start 
        else:
            # initialize a new substring index position because we found a new unique character from the string
            start = index + 1
            end = index + 1

    return valid_substring_length


if __name__ == "__main__":
    print(count("abacabb", "b")) # 7
    print(count("abcdef", "g")) # 21
    print(count("xxxxxxxxx", "x")) # 0
    print(count("pupujussikainen", "u")) # 48

"""
The idea of the solution is to go through the string from left to right and calculate at each point how many substrings ending in that point do not contain a prohibited character.

This can be done effectively by maintaining a counter that remembers how many characters in a row have not contained a prohibited character. The counter resets when a prohibited character is encountered in the string.

The resulting algorithm takes time O(n)
.

def count(s, c):
    result = 0
    counter = 0
    for i in range(len(s)):
        counter += 1
        if s[i] == c:
            counter = 0
        result += counter
    return result
"""