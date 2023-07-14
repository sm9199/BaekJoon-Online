# A + B - <7th ver.>

import sys

item = int(sys.stdin.readline())
lst = []

for i in range(item):
    num1,num2 = map(int,sys.stdin.readline().split())
    lst.append(num1+num2)
    
for i in range(item):
    print("Case #{0}: {1}".format(i+1,lst[i]))
