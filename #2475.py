# 검증 수

num = list(map(int,input().split()))
lst = []
total_num = 0

for i in range(len(num)):
    lst.append(num[i]*num[i])
    total_num = sum(lst) % 10
    
print(total_num)