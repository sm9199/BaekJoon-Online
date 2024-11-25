# 쉽게 푸는 문제

n1 , n2 = map(int, input().split())

lst = [0]

sum = 0

for i in range(1, n2+1):
    for j in range(i):
        lst.append(i)
        
for i in range(n1, n2+1):
    sum += lst[i]
    
print(sum) 