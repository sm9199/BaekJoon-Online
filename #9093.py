# 단어 뒤집기
# 자료구조 -1

n = int(input())

for _ in range(n):
    operator = list(input().split())
    for i in operator:
        print(i[::-1], end=' ')
