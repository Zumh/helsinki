#!/usr/bin/env python3

def distinct_characters(L):
    # results= {}
    # for word in L:
    #     results[word] = len(set(word))
    return {word:len(set(word)) for word in L}

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
