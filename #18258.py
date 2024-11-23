# 큐 2

# ver.1 시간 초과 발생

# import sys

# n = int(sys.stdin.readline())

# stack = []

# for i in range(n):
#     command = sys.stdin.readline().split()
    
#     if command[0] == 'push':
#         stack.append(command[1])
        
#     if command[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop(0))
            
#     if command[0] == 'size':
#         print(len(stack))
        
#     if command[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
    
#     if command[0] == 'front':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[0])
            
#     if command[0] == 'back':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack[-1])

# ==============================================

# Ver 2 deque 사용

import sys

from collections import deque

n = int(input())
queue = deque([])

for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif com[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])