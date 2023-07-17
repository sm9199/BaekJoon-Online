# 소트 인 사이드

num = int(input())
num_list = []

for i in str(num):
    num_list.append(i)
    
sorted_num_list = sorted(num_list ,reverse= True)

for j in sorted_num_list:
    print(j,end='')