# 나머지

num = 10
list = []

for i in range(num):
    nums = int(input())
    list.append(nums%42) # 애초에 리스트에 담을 때 나머지 연산을 한 결과를 바로 넣기기
list = set(list)

print(len(list))