# 창문 닫기

n = int(input())

total = 0

fir_num = 1

while fir_num*fir_num <= n:
    fir_num += 1
    total += 1
    
print(total)