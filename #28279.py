# 덱 2
import sys
from collections import deque

n = int(sys.stdin.readline())

lst = deque()

for i in range(n):
    command = sys.stdin.readline().split()
        
    if command[0] == '1':
        lst.appendleft(command[1])
    
    elif command[0] == '2':
        lst.append(command[1])
    
    elif command[0] == '3':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.popleft())
            
    elif command[0] == '4':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())
            
    elif command[0] == '5':
        print(len(lst))
    
    elif command[0] == '6':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
            
    elif command[0] == '7':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    elif command[0] == '8':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    