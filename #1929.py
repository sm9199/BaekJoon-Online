# 소수 구하기

num1 , num2 = map(int,input().split())

for i in range(num1,num2+1): # 해당하는 범위를 반복
    if i == 1: # 에라토스테네스의 체의 첫번 째 규칙. 1를 제거하기
        continue
    for j in range(2, int(i**0.5)+1): # 에라토스테너스의 체의 두번 째 규칙. 2의 배수를 제거한다.
        if i%j == 0:
            break
    
    else:
        print(i)
