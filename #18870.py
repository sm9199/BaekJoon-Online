# 좌표 압축

num = int(input())
num_list = list(map(int,input().split()))

sorted_num_list = sorted(set(num_list))

dictionary = {sorted_num_list[i] :i for i in range(len(sorted_num_list))}

for i in num_list:
    print(dictionary[i],end =' ')

