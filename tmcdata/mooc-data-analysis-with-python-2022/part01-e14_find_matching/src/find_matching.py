#!/usr/bin/env python3

def find_matching(L, pattern):

    return [index for index, value in enumerate(L) if pattern in value]

def main():
    result = find_matching(["sensitive", "engine", "rubbish", "comment"], "en") 
    print(result)
if __name__ == "__main__":
    main()
