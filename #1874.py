# 스택 수열

n = int(input())

count = 1 # 스택에 담긴 순서를 카운트
stack = [] # 숫자 담긴 스택
operation = [] # 연산 순서 담긴 스택

for i in range(n):
    num = int(input())
    
    while count <= num: # 스택에 넣고 출력할 연산만큼 반복 
        # Ex. 처음에 num = 6을 시작하면 +기호를 6번 반복하여 출력함. 
        stack.append(count)
        operation.append('+')
        count += 1
        
    if stack[-1] == num: # 맨 위에 있는 스택의 값이 num과 같다면?
        # Ex. num = 6일때 stack에 제일 위쪽에 값도 6이 된다면 빼야하니까 pop('-' 출력)을 사용한다.
        stack.pop()
        operation.append('-')
        
    else:
        print("NO")
        break
        

else:
    for i in operation:
        print(i)