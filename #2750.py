# 수 정렬하기

num = int(input())
num_list = []

for i in range(num):
    num = int(input())
    num_list.append(num)
    
NUM_list = sorted(num_list)

for j in NUM_list:
    print(j)