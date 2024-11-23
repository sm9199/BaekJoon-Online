# 상금 헌터

import sys

n = int(sys.stdin.readline())  # 참가자 수 입력

for i in range(n):
    w1 , w2 = map(int, sys.stdin.readline().split())  # 각각 1, 2차 대회 등수 입력
    
    # 첫 번째 대회의 상금 계산
    if w1 == 1:
        w1 = 5000000
    elif 1 < w1 < 4:
        w1 = 3000000
    elif 3 < w1 < 7:
        w1 = 2000000
    elif 6 < w1 < 11:
        w1 = 500000
    elif 10 < w1 < 16:
        w1 = 300000
    elif 15 < w1 < 22:
        w1 = 100000
    else:
        w1 = 0  # 상금 대상 외

    # 두 번째 대회의 상금 계산
    if w2 == 1:
        w2 = 5120000
    elif 1 < w2 < 4:
        w2 = 2560000
    elif 3 < w2 < 8:
        w2 = 1280000
    elif 7 < w2 < 16:
        w2 = 640000
    elif 15 < w2 < 32:
        w2 = 320000
    else:
        w2 = 0  # 상금 대상 외
    
    # 각 참가자별 상금 합계 출력
    print(w1 + w2)
