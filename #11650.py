# 좌표 정렬하기

xy_count = int(input())
xy_list = []

for _ in range(xy_count): 
    x,y = map(int,input().split())
    xy_list.append((x,y)) # (x,y)를 해줌으로써 x,y를 한번에 담을 수 있다.

xy_list.sort() # (x,y) 정렬시켜준다.

for i in range(xy_count): 
    print(xy_list[i][0],xy_list[i][1]) # 정렬 된 것을 순차적으로 출력하기위함.
    # [i][0] 과 [i][1]을 통해 해당되는 자리를 출력시키게 해줌.
    