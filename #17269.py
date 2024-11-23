# 이름궁합 테스트
import copy

# 딕셔너리 사용
dic = {'A':3,'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}

# 이름 길이 기입
n_len1 , n_len2 = map(int, input().split())

# 이름 생성
n1 , n2 = input().split()

# 두 이름의 길이 중 최소를 잡음(이름이 긴 사람은 뒤에 붙이기 용)
min_len = min(n_len1, n_len2)

word = []

for i in range(min_len):
    word += n1[i] + n2[i]
    
if n_len1 > n_len2:
    word += n1[min_len:]
elif n_len1 < n_len2:
    word += n2[min_len:]
    
new_word = []

for j in word:
    new_word.append(dic[j])
    
while len(new_word) > 2:
    temp = []
    for k in range(1, len(new_word)):
        temp_num = new_word[k-1] + new_word[k]
        if temp_num >= 10:
            temp_num -= 10
        temp.append(temp_num)
    new_word = copy.deepcopy(temp)
    
print("{}%".format(new_word[0]*10 + new_word[1]))