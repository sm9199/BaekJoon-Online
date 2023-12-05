# 수 정렬하기 2
# 2750번 문제보다 빠르게 처리하는 방법

import sys

num = int(input())
num_lst = []
for _ in range(num):
    num_lst.append(int(sys.stdin.readline()))

num_lst.sort()

for i in num_lst:
    print(i)