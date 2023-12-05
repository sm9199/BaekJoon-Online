# 문자열 집합

num_count , num_len = map(int,input().split())
count = 0
s= set()

for _ in range(num_count):
    sentence = input().rstrip()
    s.add(sentence)
    
for _ in range(num_len):
    sentence = input().rstrip()
    if sentence in s:
        count += 1
        
print(count)