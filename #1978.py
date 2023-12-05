# 소수 찾기

num = int(input())
real_num = map(int,input().split())
count = 0

for i in real_num:
    error_count = 0
    if i ==1:
        continue
    for j in range(2,i+1):
        if i%j ==0:
            error_count +=1
    if error_count == 1:
        count += 1
        
print(count)
        
    