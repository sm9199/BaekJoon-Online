# 알파벳 찾기

keyword = input()

data = 'abcdefghijklmnopqrstuvwxyz'
data = list(data)

for i in data:
    print(keyword.find(i))