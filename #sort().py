# sort()에서의 key lambda 사용 연습

num_list = [(1,2),(0,1),(5,1),(5,2),(3,0)]

# 1. 인자 없이 그냥 sort함수를 사용한다면 , 리스트 원소 순서대로 정렬함.
#num_list.sort()
# sorted_num_list = sorted(num_list)
#print(num_list) 
# 결과 출력 : [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# 2. key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬함.
# num_list.sort(key=lambda x : x[0])
# print(num_list)
# 결과 출력 : [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# num_list.sort(key=lambda x : x[1])
# print(num_list)
# 결과 출력 : [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

# 3. 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬 한 후,
# 그 안에서 다음 두번째 인자 기준으로 내림차순으로 정렬하게 한다.
num_list2 = [(1,3),(0,3),(1,4),(1,5),(0,1),(2,4)]
num_list2.sort(key=lambda x : (x[0],-x[1]))
print(num_list2)
# 결과 출력 : [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]