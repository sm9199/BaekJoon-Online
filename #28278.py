# 스택 2

import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == '1':
        stack.append(command[1])
    if command[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print("-1")
    if command[0] == '3':
        print(len(stack))
    if command[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    if command[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)