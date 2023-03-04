"""
Implement the efficiency test described in section 2.1.4 of the course book on your own computer. Implement algorithms with Python and measure their execution time when: n=105. In the test, use a random input with the character 0 and 1The probability of being elected is equal.

A good way to measure code execution time is to ask the time moment on the system clock just before and after code execution. The difference between these moments of time tells you how long it took to run the code.

To use the module function, follow these steps: Note that in the course book,
the comparison is implemented in Java, which is a faster language than Python. Therefore, you can be prepared for the fact that your own test will take more time than the results of the book.

In this task, you will automatically get a point when you indicate the results and the code you are using and press the submit button.

import time

alku = time.time()
# testattava koodi
loppu = time.time()
print("aikaa kului", loppu-alku, "s")

laskuri = 0
for i = 0 to n-1:
    for j = i+1 to n-1:
        if merkit[i] == 0 and merkit[j] == 1:
            laskuri += 1
print(laskuri)


laskuri = 0
nollat = 0
for i = 0 to n-1
    if merkit[i] == 0
        nollat += 1
    else
        laskuri += nollat
print(laskuri)
"""


import time
characters = [0,1,0,0,1]
n = len(characters)
counter = 0
start = time.time()
# code to test
for i in range(n):

    for j in range(i+1, n):
        if characters[i] == 0 and characters[j] == 1:
            counter += 1
print(counter)
end = time.time()
print("o(n^2) time elapsed", end-start, "s")

counter = 0
zeros = 0
start = time.time()
# code to test
for i in range(n):
    if characters[i] == 0:
        zeros += 1
    else:
        counter += zeros
print(counter)
end = time.time()
print("o(n) time elapsed", end-start, "s")