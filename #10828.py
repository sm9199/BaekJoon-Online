# 스택
# split을 활용한 리스트 이용하기
import sys 

num = int(sys.stdin.readline())

lst = [] # 스택 형식을 리스트로 구현함.

for i in range(num): # 명령어를 num 횟수만큼 반복
    
    a = sys.stdin.readline().split()
    
    if a[0] == 'push':
        lst.append(a[1])
        
    elif a[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())
            
    elif a[0] == 'size':
        print(len(lst))
        
    elif a[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
        
    elif a[0] == 'top':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])