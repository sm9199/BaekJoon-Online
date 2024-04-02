# 괄호
# 자료구조 -1

n = int(input())

for _ in range(n):
    character = input()
    a = character.count('(')
    b = character.count(')')
    
    
    
for i in range(n):
    if a == b:
        print("YES")
        
    else:
        print("NO")
