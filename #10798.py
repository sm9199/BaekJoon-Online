# 세로읽기

a = [[0] * 15 for i in range(5)] # 빈칸을 우선 0으로 설정한 5x15 행렬 만든다.

for i in range(5):  # 5줄을 생성
    w = list(input()) # 변수 w을 리스트 형식으로 문자를 넣음 
    w_len = len(w) # 변수의 총 길이

    for j in range(w_len): # 변수의 총 길이만큼 반복
        a[i][j] = w[j] 

for i in range(15):
    for j in range(5):

        if a[j][i] == 0:
            continue;

        else:
            print(a[j][i], end='')