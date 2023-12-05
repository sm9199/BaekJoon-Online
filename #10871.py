# X보다 작은 수

total_num, avr_num = map(int,(input().split())) # 숫자 총 갯수와 기준이 되는 숫자를 map형식으로 초기화

num = list(map(int,input().split())) # 숫자 총 개수에 맞추어 list 형태로 숫자를 추가

for i in range(total_num): # 숫자 총 개수만큼 반복을 함
    if num[i]<avr_num: # 배열 안에 원소들의 값이 기준이 되는 숫자보다 작을때
        print(num[i],end=" ") # 해당되는 숫자를 출력하고 end를 이용해 마지막에 띄어 쓰기를 포함시킨다.