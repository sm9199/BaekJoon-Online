# 수 정렬하기 3

# ver.1 -> 메모리 초과
# num_count = int(input())
# num_list = []
# for i in range(num_count):
#     num = int(input())
#     num_list.append(num)

# sorted_list = sorted(num_list)

# for j in sorted_list: 
#     print(j)

###################################################
# ver.2 -> sys 을 사용했음에도 메모리 초과(sort함수가 메모리 초과시킨다!!!)
# import sys

# num_count = int(sys.stdin.readline())
# num_list = []

# for i in range(num_count):
#     num_list.append(int(sys.stdin.readline()))

# sorted_list = sorted(num_list)

# for j in sorted_list: 
#     print(j)

##################################################
# ver.3 -> 계수 정렬

import sys
num_count = int(sys.stdin.readline())
num_list  = [0] * 10001 # 리스트의 10000개 자리를 0으로 초기화 시킨다.

for i in range(num_count):
    num_list[int(sys.stdin.readline())] += 1 # 정렬하려는 해당 값에 1을 더해준다. 
    
for j in range(10001):
    if num_list[j] != 0:
        for k in range(num_list[j]):
            print(j)
