# 대칭 차집합

# set 함수(집합, 중복되지 않은 원소를 얻고자 할 때 사용하는 함수)

num1, num2 = map(int, input().split())

lst_1 = set(map(int, input().split())) # list 안에 값 원소 추가(중복 불가)
lst_2 = set(map(int, input().split()))

# list안에 있는 원소들의 중복 제거
print(len(lst_1 - lst_2) + len(lst_2 - lst_1)) 

