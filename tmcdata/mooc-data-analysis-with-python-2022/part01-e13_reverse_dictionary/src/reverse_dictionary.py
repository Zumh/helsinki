#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}
    for key, values in d.items():
        for value in values:
            if value not in result:
                result[value] = [key] 
            else:
                result[value].append(key)
        
    return result

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
