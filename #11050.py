# 이항계수 1

n1 , n2 = map(int, input().split())

result = 1
for i in range(n2):
    result *= n1
    n1 -= 1
    
divisor = 1

for i in range(2, n2+1):
    divisor *= i
    
    
print(result// divisor)