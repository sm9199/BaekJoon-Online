# 벌집

num = int(input())

start_num = 1 # 벌집 시작 숫자
count = 1 # 벌집의 겹수

while num > start_num: # 해당되는 임의의 숫자가 벌집 시작 숫자보다 클때
    start_num += 6*count # 벌집 숫자가 6의 배수로 증가
    count += 1 # 벌집 겹수가 1씩 증가함.
    
print(count)