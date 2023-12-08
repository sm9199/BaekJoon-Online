# 서로 다른 부분 문자열의 개수

n = input()

total = set()

for i in range(len(n)):
    for j in range(i, len(n)):
        temp=n[i:j+1]
        total.add(temp)
        
print(len(total))
