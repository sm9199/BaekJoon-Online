# 나이 순 정렬

member = int(input())
member_list = []

for _ in range(member):
    age , name = input().split()
    age = int(age)
    member_list.append((age,name))
    
member_list.sort(key=lambda x : x[0])

for a,b in member_list:
    print(a,b)