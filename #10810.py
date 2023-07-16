# 공 넣기

busket,ball = map(int,input().split())
list = [0] * (busket+1)

for i in range(ball):
    num_busket_1 , num_busket_2 , num_ball = map(int,input().split())
    for j in range(num_busket_1,num_busket_2+1):
        list[j] = num_ball
        
for num_busket_1 in range(1,busket+1):
    print(list[num_busket_1],end = ' ')
