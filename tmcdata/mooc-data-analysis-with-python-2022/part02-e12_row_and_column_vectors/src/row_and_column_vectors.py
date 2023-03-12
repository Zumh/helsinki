#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
   
    return [number.reshape(1,len(a[0,:])) for number in a]

def get_column_vectors(a):
    return [column.reshape(len(a[:,0]), 1) for column in a.T]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()

"""
Better solution 
def get_row_vectors(a):
    # (1,m) shape[0] number is for horizontal axis only
    return np.split(a, a.shape[0], axis=0)
 
def get_column_vectors(a):
    # (n,1) shape[1] number is for column axis only
    return np.split(a, a.shape[1], axis=1)
"""
