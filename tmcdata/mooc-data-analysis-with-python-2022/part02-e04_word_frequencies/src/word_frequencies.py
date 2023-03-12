#!/usr/bin/env python3

def word_frequencies(filename = "alice.txt"):
    result = {}

    with open(filename, 'r') as file_content:
        for line in file_content:
            for word in [word.strip("""!"#$%&'()*,-./:;?@[]_""") for word in line.split()]:
                if word not in result:
                    result[word] = 0
                result[word] += 1
    
    return result

def main():
    word_frequencies()

if __name__ == "__main__":
    main()
