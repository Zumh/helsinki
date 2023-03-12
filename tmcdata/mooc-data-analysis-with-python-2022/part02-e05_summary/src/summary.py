#!/usr/bin/env python3

import sys
from math import sqrt

def summary(filename):
    total_number, average, std_deviation = 0, 0, 0
    count_number = 0
    numbers = None
    with open(filename, 'r') as content:
        numbers = content.read()
       
    data = []
    for number in numbers.strip().split('\n'):
        try:
            converted_number = float(number)
            data.append(converted_number)
        except ValueError:
            pass    

    total_number = sum(data)
    data_length = len(data)
    average = total_number/data_length
    
    for index in range(0, data_length):
        deviation = data[index] - average
        std_deviation += deviation**2
    std_deviation = sqrt(std_deviation/(data_length - 1))

    """
    n = length(data)
    mean = sum(data) / n
    sum_of_squared_deviations = 0
    for i = 1 to n:
        deviation = data[i] - mean
        sum_of_squared_deviations += deviation * deviation
    sample_variance = sum_of_squared_deviations / (n - 1)
    sample_standard_deviation = square_root(sample_variance)
    """
    return (total_number, average, std_deviation)

def main():
    
    for file_name in sys.argv[1:]:
         print('File: {} Sum: {:0.6f} Average: {:0.6f} Stddev: {:0.6f}'.format(file_name,*summary("src/"+file_name)))

if __name__ == "__main__":
    main()

"""
# model solution
from statistics import stdev
import sys
 
def summary(filename):
    L=[]
    with open(filename) as f:
        for line in f:
            try:
                L.append(float(line))
            except ValueError:
                continue
    s = sum(L)
    a = s/len(L)
    stddev = stdev(L)
    return s, a, stddev
"""
