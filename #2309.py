# 일곱 난쟁이

lst = []
sum = 0

for i in range(9):
    lst.append(int(input()))

lst.sort()

for j in range(9):
    sum += lst[j]
    
    if sum == 100:
        print(lst[j]) 