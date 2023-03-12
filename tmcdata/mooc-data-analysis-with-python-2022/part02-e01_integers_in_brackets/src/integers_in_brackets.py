#!/usr/bin/env python3

import re 
def integers_in_brackets(s):
    pattern = r'\[(\s*[+-]?\d+)\s*\]'
    result = list(map(int, re.findall(pattern, s)))
    return result

def main():
    result = integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")
    print(result)
if __name__ == "__main__":
    main()
