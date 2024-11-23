# 누울 자리를 찾아라

n = int(input())

lst = [list(input().strip()) for _  in range(n)]

location = [0,0]

for i in range(n):
    width , height = 0 , 0
    for j in range(n):
        # 가로
        if lst[i][j] == '.':
            width += 1
        else:
            width = 0
            
        if width == 2:
            location[0] += 1
            
        # 세로
        if lst[j][i] == '.':
            height += 1
        else:
            height = 0
            
        if height == 2:
            location[1] += 1
            
print(*location)
            