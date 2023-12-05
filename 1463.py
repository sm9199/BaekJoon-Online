# 1로 만들기

x=int(input()) # 수 입력받기
d=[0]*(x+1) # 1-based[x에 1을 넣을 때 값은 이미 충족해서 계산 횟수 0으로 출력]

for i in range(2,x+1): # 2부터 x까지 반복
    d[i]=d[i-1]+1 # 1을 빼는 연산 -> 1회 진행
    if i%2==0: # 2로 나누어 떨어질 때, 2로 나누는 연산
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0: # 3으로 나누어 떨어질 때, 3으로 나누는 연산
        d[i]=min(d[i],d[i//3]+1)
print(d[x])