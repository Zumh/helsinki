"""
Your task is to encrypt the given string so that the first character moves in the alphabet one character forward, the second character two characters forward, the third character three characters forward, etc. If the character grows larger than , it will again return to the beginning of the alphabet.

A string is made up of characters – and contains up to 100 characters.

Implement a function in the file that produces an encrypted string.
Explanation: In a string, a character greater than one of the characters is . A character equal to the character is , because after , we move back to the beginning of the alphabet. Thus, a character larger than two is . Therefore, the string is encrypted . zazencryption.pyencrypt
"""

def encrypt(s):
    encrypted_string = ""
    offset = 1
    alphabet_length = 26
    a_ascii = 97
    A_ascii = 65

    """
    encrypted forumla:
    if a letter in a string is lower case then we start with 97
    first we offset base on starting ascii value = offset - a_ascii
    then we add current letter ascii value so that it will offset from current letter
    ord(letter) + offset - a_ascii
    then we wraps it around if we end up more than 'z' to the beginning by finding mod 26 letters.
    (ord(letter) + offset - a_ascii)) % 26
    then we add start of ascii value back to get correct offset from the start
    (ord(letter) + offset - a_ascii)) % 26 + a_ascii
    """
    for letter in s:
        if letter.isupper():
            encrypted_string += chr((ord(letter) + offset - A_ascii)%26 + A_ascii)
        elif letter.islower():
            encrypted_string += chr((ord(letter) + offset - a_ascii)%26 + a_ascii)
        offset += 1
    return(encrypted_string)
if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # bcdefghijklmnopqrstuvwxyzabcde
