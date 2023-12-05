# 그룹 단어 체커

num_word = int(input()) # 그룹 단어의 개수 출력
count = num_word # 카운트를 세는데 처음에는 num_word로 초기화

for i in range(num_word): # 그룹 단어의 개수만큼 반복
     word = input() # 단어 기입
     for j in range(len(word)-1): # len(word)-1 을 해주는 이유는 밑의 조건문을 통해 j와 j+1을 비교하니까.
         if word[j]==word[j+1]:
             continue # 같은 문자가 반복해서 나올때는 그룹단어 인정
         elif word[j] in word[j+1:]: # word[j]번째가 j+1부터 끝까지 반복해서 중복되는 값이 포함이 될떄
             count -= 1 # 카운트 하나 제거
             break 
         
print(count)