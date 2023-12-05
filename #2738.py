# 행렬 덧셈

a,b = [],[] # a,b의 2차원 배열을 만들 준비
n,m = map(int,input().split()) # _x_ 행렬을 정해주는 변수

for _ in range(n): # 행의 수만큼 반복
    row = list(map(int,input().split())) # 2차원 배열 a에 원소 넣기
    a.append(row) # 추가
    
for _ in range(n): # 
    row = list(map(int,input().split()))
    b.append(row)
    
for row in range(n):
    for col in range(m):
        print(a[row][col] + b[row][col], end = ' ')
    print()