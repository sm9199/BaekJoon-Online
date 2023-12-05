#공 바꾸기


busket,change_times = map(int,input().split())
ball = []

for i in range(0,busket+1):
    ball.append(i)  
for j in range(change_times):
    num_busket_1,num_busket_2 = map(int,input().split())
    ball[num_busket_1],ball[num_busket_2] = ball[num_busket_2] , ball[num_busket_1]

print(*ball[1:])