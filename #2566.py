# 최댓값

mx = 0 
v = -1 
for i in range(9): # 반복문
    num = list(map(int,input().split())) # 숫자대입
    mx = max(num) # 각 행의 최대값을 비교
    if mx > v: # mx의 값이 초기화시킨 v(-1)값보다 클 때
        v = max(num) # 최댓값 갱신
        row = i + 1 # 최댓값 판별 후 최댓값 해당되는 행을 출력
        col = num.index(v) + 1 # 최댓값 판별 후 최댓값 해당되는 열을 출력 
print(v)
print(row, col)