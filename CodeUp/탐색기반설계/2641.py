# 2641 : 숏다리의 계단 오르기 (Small)

# 계단의 수 n
n = int(input())

count = 0

def stair(total, up):
    global result
    
    up -= 1
    
    if n == 0:
        return 0
    elif n - total >= 1 : stair(total+1, up)