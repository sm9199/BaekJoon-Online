# 주사위 게임
dice = int(input())
total = 0

for _ in range(dice):
    x,y,z = map(int,input().split())

    if x == y == z:
        total = max(total, 10000 + x*1000)
    elif x == y:
        total = max(total, 1000 + x*100)
    elif x == z:
        total = max(total, 1000 + x*100)
    elif y == z:
        total = max(total, 1000 + y*100)
    else:
        total = max(total,  max(x,y,z) * 100 )

print(total)
