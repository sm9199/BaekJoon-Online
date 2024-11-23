# 수빈이와 수열

import sys

n = int(sys.stdin.readline()) 
array = list(map(int, input().split()))
seq = [array[0]]

for i in range(1, n):
    seq.append(array[i] * (i+1) - sum(seq))
for i in seq:
    print(i , end = ' ')
    

