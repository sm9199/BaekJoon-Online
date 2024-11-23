# 카드 2

import sys

from collections import deque

n = int(sys.stdin.readline())

stack = deque(range(1,n+1))

while (len(stack) > 1):
    stack.popleft()
    stack.append(stack.popleft())    

print(stack.popleft())