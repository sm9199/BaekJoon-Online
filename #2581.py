# 소수

first_num = int(input())
second_num = int(input())
arr = []

for i in range(first_num,second_num+1):
    err_count = 0
    if i > 1:
        for j in range(2,i):
            if (i%j==0):
                err_count +=1
                break
        if err_count == 0:
            arr.append(i)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)