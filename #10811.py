# 바구니 뒤집기

basket,swap = map(int,input().split())
list = []

for i in range(1,basket+1):
    list.append(i)
for j in range(swap):
    a,b = map(int,input().split())
    # list[a-1],list[b-1] = list[b-1],list[a-1]
    list[a-1:b]=list[a-1:b][::-1]
    
print(*list)