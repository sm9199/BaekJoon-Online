# 영수증

total_price = int(input())
total_item = int(input())
sum = 0

for i in range(total_item):
    price,item = map(int,input().split())
    sum += price*item
    
if sum == total_price:
    print("Yes")
else:
    print("No")
