# A + B - <8th ver.>

import sys

item = int(sys.stdin.readline())
lst = []

for i in range(item):
    num1,num2 = map(int,sys.stdin.readline().split())
    lst.append(num1+num2)
    print("Case #{0}: {1} + {2} = {3}".format(i+1,num1,num2,lst[i]))
