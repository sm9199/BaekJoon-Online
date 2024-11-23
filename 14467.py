# 소가 길을 건너간 이유 1

import sys

# 소의 n의 마리 설정
n = int(input())

# 모든 소의 위치를 -1으로 초기화하기
cows = [-1] * 11

# 소의 위치가 바뀌었을 때 카운트 증가
count = 0

# 소의 1번마부터 n번마 까지 반복
for i in range(n):
    cow, loc = map(int, input().split())
    
    # 초기 위치가 -1이므로
    if cows[cow] == -1:
        # cows[cow]의 값이 -1에서 loc(위치 값)으로 바꿈
        cows[cow] = loc
    else:
        if cows[cow] != loc:
            count += 1
            cows[cow] = loc
            
print(count)
