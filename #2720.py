# 세탁소 사장 동혁

change = [25,10,5,1]

test_time = int(input())

for _ in range(test_time):
    money = int(input())
    money_list = []
    
    for i in change:
        money_list.append(money//i)
        money = money % i
        
    print(*money_list)