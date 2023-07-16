# 문자열 반복

num = int(input())

for _ in range(num):
    n,s = input().split()
    for c in s:
        print(c*int(n), end = '')
    print()