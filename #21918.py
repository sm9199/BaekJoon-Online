# 전구 - Bronze 2

a, b = map(int, input().split())

lst = list(map(int, input().split()))


for i in range(b):
    function = list(map(int, input().split()))
    
    if function[0] == 1:
        lst[function[1]-1] = function[2]
        
    elif function[0] == 2:
        for j in range(function[1]-1, function[2]):
            if lst[j] == 0:
                lst[j] = 1
            else:
                lst[j] = 0

    elif function[0] == 3:
        for j in range(function[1]-1 , function[2]):
            if lst[j] == 1:
                lst[j] = 0
    
    elif function[0] == 4:
        for j in range(function[1]-1 , function[2]):
            if lst[j] == 0:
                lst[j] = 1
                
print(*lst)
