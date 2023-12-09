# 서로 다른 부분 문자열의 개수

n = input()

total = set() # 중복을 사라지게 함

# 이중 반복문을 통해 문자열이 될 수 있는 모든 경우의 수를 구함
for i in range(len(n)): # 첫번째 문자부터 기준을 잡아놓는다. 
    for j in range(i, len(n)): # 두번째 문자는 1씩 증가시켜 문자열의 범위를 늘림
        temp=n[i:j+1] # 문자열 생성
        total.add(temp) # 임시로 담을 temp에 모든 경우의 문자열을 다 담아놓음 
        
print(len(total)) # total에 set함수를 사용하여 중복되는 값 제거
