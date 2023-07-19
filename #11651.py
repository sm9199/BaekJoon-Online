# 좌표 정렬하기 -2

xy_count = int(input())
xy_list = []


for i in range(xy_count):
    x,y = map(int,input().split())
    xy_list.append((y,x))
    
sorted_xy_list = sorted(xy_list)

for y,x in sorted_xy_list:
    print(x,y)
    
    