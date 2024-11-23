# 오큰수

# 수열에서 NGE(N)기준 N보다 큰 수중 가장 왼쪽에 위치한 수를 찾기

# 수열 크기 설정
n = int(input())

# 리스트 형식으로 수열을 저장
seq = list(map(int,input().split()))

# 결과값을 담을 리스트 생성
lst = []

# nge값이 없을 때는 -1으로 설정하므로 초기에 -1으로 설정
nge = [-1] * n

# 결과값에 0을 추가
lst.append(0)

for i in range(1, n):
    while lst and seq[lst[-1]] < seq[i]:
        nge[lst.pop()] = seq[i]
    lst.append(i)   
    
print(*nge)    