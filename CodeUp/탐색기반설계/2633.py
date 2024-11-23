# 2633 : Lower Bound

n1, n2 = map(int, input().split())

k = list(map(int, input().split()))
    
for i in range(n1):
    if k[i] >= n2:
        print(i+1)
        break  
    
if k[i] < n2:
    print(n1+1)

