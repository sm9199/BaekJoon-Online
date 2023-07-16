# 단어 공부

words = input().upper() # 원하는 단어 입력

s_sets = list(set(words)) # 리스트형으로 중복되지 않게 문자열 저장

lst = [] # 새로운 리스트 구현

for i in s_sets: # 중복되지 않은 단어개수만큼 반복시킨다.
    lst.append(words.count(i)) # 초기 단어(중복 포함)한 단어의 개수를 하나씩 계산한다.
if lst.count(max(lst))>1: # 특정한 알파벳이 가장 많이 사용한 경우가 2번이상이라면
    print("?")
else:
    print(s_sets[lst.index(max(lst))]) # s_sets에 담겨있는 중복되지 않은 문자열에서 lst의 인덱스값(자리가 서로 같기 때문에)
    # 가장 큰 lst값을 출력하게 된다.