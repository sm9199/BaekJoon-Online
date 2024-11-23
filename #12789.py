# 도키도키 간식드리미
import sys

# 학생 수
n = int(sys.stdin.readline())

# 학생들이 뽑은 번호표
students = list(map(int,input().split()))

# 한명씩 설 수 있는 공간(스택)
stack = [] 

# 번호표 시작 번호
turn = 1

# 학생들으 한명씩 설 수 있는 공간 생성 후 담기
for i in students:
    stack.append(i)
    
    # 스택의 현재와 마지막 부분이 turn과 같을 때 번호표 대로 빠지기
    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1
        

if stack:
    print('Sad')
else:
    print("Nice")
