# 대지 (그래프)

circle_num = int(input())

lst_x = []
lst_y = []

for _ in range(circle_num):
    x,y = map(int,input().split())
    lst_x.append(x)
    lst_y.append(y)
    
    
print((max(lst_x)-min(lst_x))*(max(lst_y)-min(lst_y)))