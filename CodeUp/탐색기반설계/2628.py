# 2628 : 케익 자르기

n1, n2 = map(int,input().split())
n3, n4 = map(int,input().split())

if n1 > n2:
    n1 ,n2  = n2, n1
    
count = 0

for i in n3, n4:
    if n1 < i < n2:
        count += 1
        
if count == 1:
    print("cross")
else:
    print('not cross')