# 괄호
# 자료구조 -1
## Silver(4)

# 단순하게 괄호 갯수만 세서 했더니 )( 모양도 Yes가 나오는 현상이 나타남.
# n = int(input())

# for _ in range(n):
#     character = input()
#     a = character.count('(')
#     b = character.count(')')
    
    
    
# for i in range(n):
#     if a == b:
#         print("YES")
        
#     else:
#         print("NO")


n = int(input())

for i in range(n):
    lst = []
    ch = input()
    for j in ch:
        if j == '(':
            lst.append(j)
        elif j == ')':
            if len(lst) != 0:
                lst.pop()
            else:
                print("NO")
                break
    else:
        if len(lst) == 0:
            print("YES")
        else:
            print("NO")