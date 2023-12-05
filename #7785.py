# 회사에 있는 사람
import sys

people = int(sys.stdin.readline())
dic = {}

for _ in range(people):
    person,state = sys.stdin.readline().split()
    dic[person] = state
    if state == "leave":
        del dic[person]
        
d = sorted(dic.items(),reverse=True)
dic = dict(d)

for key in dic.keys():
    print(key)