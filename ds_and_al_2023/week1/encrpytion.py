"""
Your task is to encrypt the given string so that the first character moves in the alphabet one character forward, the second character two characters forward, the third character three characters forward, etc. If the character grows larger than , it will again return to the beginning of the alphabet.

A string is made up of characters – and contains up to 100 characters.

Implement a function in the file that produces an encrypted string.
Explanation: In a string, a character greater than one of the characters is . A character equal to the character is , because after , we move back to the beginning of the alphabet. Thus, a character larger than two is . Therefore, the string is encrypted . zazencryption.pyencrypt
"""

def encrypt(s):
      
if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # bdf
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # bcdefghijklmnopqrstuvwxyzabcde
