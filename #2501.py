# 약수 구하기

num, count = map(int,input().split())
divide_num = 1
zero = []

for _ in range(num):
    if (num % divide_num == 0):
        zero.append(divide_num)
    divide_num += 1

if len(zero)>=count:
    print(zero[count-1])
else:
    print(0)
    
# num, count = map(int,input().split())
# zero = []

# for i in range(1,num+1,1):
#     if (num % i == 0):
#         zero.append(i)

# if len(zero)>=count:
#     print(zero[count-1])
# else:
#     print(0)