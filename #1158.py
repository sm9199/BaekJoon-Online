# 요세푸스 문제

num1 , num2 = map(int,input().split())
lst = []
answer = []

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