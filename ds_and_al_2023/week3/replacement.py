from random import randint 
import time 

n = 10**5
start = time.time()
table = [randint(1, n) for number in range(n)]

def merge_sort(a,b):
    if a == b:
        return
    k = (a+b)/2
    merge_sort(a,k)
    merge_sort(k+1,b)
    interleave(a,k,k+1,b)
    

end = time.time()
print("time elapsed", end-start, "s")