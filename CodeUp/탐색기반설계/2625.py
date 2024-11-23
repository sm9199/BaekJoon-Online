# 2625 : 삼각화단 만들기 (Small)

n = int(input())

count = 0

for a in range(n,0,-1):
    if n-a > a: # 밑변 길이 <  두변의 길이 총합
        for b in range(n-a,0,-1):
            c = n-a-b
            if c != 0 and a >= b and b >= c:
                count += 1
    
print(count)