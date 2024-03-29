# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

Result = list(str(A*B*C)) # 세개의 숫자를 곱한 값을 문자열(str) 형식으로 변환 후 리스트형식으로 저장

for i in range(10): # 0~9 까지 숫자를 반복시킨다.
    print(Result.count(str(i))) # 각 숫자에 해당되는 횟수를 출력

