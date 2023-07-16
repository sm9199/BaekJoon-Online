# 바구니 순서 뒤집기

basket,change = map(int,input().split())
lst = []
for y in range(1,basket+1):
    lst.append(y)
    
for i in range(change):
    i,j,k = map(int,input().split())
    lst = lst[:i-1]+lst[k-1:j]+lst[i-1:k-1]+lst[j:]

print(*lst)

