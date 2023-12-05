# 색종이

color_paper_count = int(input())
array = [[0]*100 for _ in range(100)] # 0을 채운 후 100x100 행렬 생성

for i in range(color_paper_count): # 색종이 갯수만큼 반복
    paper_x,paper_y = list(map(int,input().split())) # x,y축 기준 색종이 생성
    
    for j in range(paper_x,paper_x+10): # 색종이 x축 기준 부터 10만큼 떨어진 길이까지 반복시킴
        for k in range(paper_y,paper_y+10): # 색종이 y축 기준 부터 10만큼 떨어진 길이까지 반복시킴
            array[j][k]=1 # 해당되는 범위는 1로 설정한다. (넓이 채워짐)
            
area = 0
for l in range(100): # 100만큼 반복시켜 중복되는 값 찾기
    area += array[l].count(1) # 해당되는 1의 개수를 세어 중복되는 값을 더 세지 않게 count 함수로 사용
    
print(area)