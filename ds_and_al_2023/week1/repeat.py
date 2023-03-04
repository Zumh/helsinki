"""
Simplify the problem:
The function find takes a string s as input and returns the length of the shortest substring that can be repeated to form the original string.

The function first checks all possible substring lengths from 1 to the length of the string, and for each length i, it checks if the string can be formed by repeating the substring i times. If a substring is found that can be repeated to form the original string, the function returns its length. If no such substring is found, the function returns the length of the original string.
"""
def find(s):
    string_len = len(s)
    for index in range(1, string_len+1): 
        # find the shortest substring index position number that can form original string
        # similarly the goal is finding index position that can make the whole original string
        if string_len % index == 0:
            # the if condition check if we find evenly divided substring 
            sub_string = s[:index]*(string_len//index)
            # we extract the sub_stracting, tryin to make sub string match with original string's pattern.
            if sub_string == s:
                # if both are the same we found our sub string position that form original string
                return index
if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7
"""
better solution
The solution goes through all the options from the shortest to the longest, which is the length of the string to be repeated. When a repeatable string is found, the solution returns its length.
def find(s):
    n = len(s)
    for i in range(1, n+1):
        if n%i == 0 and s[:i] * (n//i) == s:
            return i
"""