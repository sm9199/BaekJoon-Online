# 듣보잡

num1, num2 = map(int,input().split())

lst_1 = set()

for i in range(num1):
    lst_1.add(input())
    
lst_2 = set()
for i in range(num2):
    lst_2.add(input())
    
result = sorted(list(lst_1 & lst_2))

print(len(result))

for i in result:
    print(i)