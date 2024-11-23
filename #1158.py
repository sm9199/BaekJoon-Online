# 요세푸스 문제
# 리스트 2개로 풀이하는 문제

num1 , num2 = map(int,input().split())
lst = [] # 처음 순서대로 앉아있는 번호
answer = [] # 뽑힌 사람들을 순서대로 넣기 위한 리스트 생성

i = 0
num = 0 # 뽑아 낼 사람 인덱스 번호 초기화

for i in range(1, num1+1):
    lst.append(i) # 맨 처음에 앉아있는 사람들
    
for j in range(num1):
    num += num2 -1
    if num >= len(lst):
        num = num % len(lst)
        
    answer.append(str(lst.pop(num)))
    
print("<",", ".join(answer)[:],">", sep='')