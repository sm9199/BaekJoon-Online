# 에디터

# 시간 복잡도
# append() : O(1)
# pop() : O(1)
# insert() : O(N)

## insert 쓰는 것 보다 
## append나 pop함수를 사용해서 stack을 2개로 만들자


import sys

offer = list(input().strip()) # 입력할 문자열 
offer2 = []

n = int(sys.stdin.readline()) # 명령어 사용할 횟수
cursor = len(offer) # 문자열의 길이

for i in range(n):
    command = list(sys.stdin.readline().split())
    
    if command[0] == 'P': 
        offer.insert(cursor, command[1]) # cursor(문자열 개수) 앞에 출력
        cursor += 1 # 명령어 P는 어떤 문자열을 하나 추가했으므로 cursor도 1 증가 시킨다.
            
    elif command[0] == 'L':
        if offer:
            offer2.append(offer.pop())
            
    elif command[0] == 'D':
        if offer2:
            offer.append(offer2.pop())
            
    elif command[0] == 'B':
        if offer:
            offer.pop()
            
answer = offer + offer2[::-1]
print(''.join(answer), end = '')