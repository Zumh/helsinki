#!/usr/bin/env python3

import numpy as np

def diamond(n):
    right_box = np.eye(n, dtype = int)
    return np.array(np.concatenate((right_box, right_box),axis=1))

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()
