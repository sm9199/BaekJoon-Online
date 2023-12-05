# 팰린도롬인지 확인하기

word = list(input())

if word == word[::-1]:
    print(1)
else:
    print(0)