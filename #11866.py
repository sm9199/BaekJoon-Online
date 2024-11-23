# 요세푸스 문제 0

import sys
from collections import deque

queue = deque()
lst = []

n1, n2 = map(int, sys.stdin.readline().split())

for i in range(1,n1+1):
    queue.append(i)


while len(queue) != 0:
    for i in range(n2-1):
        queue.append(queue.popleft())
    lst.append(queue.popleft())


print("<", end='')
print(', '.join(map(str,lst)), end='')
print(">")