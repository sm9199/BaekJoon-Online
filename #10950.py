# A + B - <3단계 ver>
word = int(input())
lst = []

for i in range(word):
    num1,num2 = map(int,input().split())
    lst.append(num1+num2)
    
for i in range(word):
    print(lst[i])