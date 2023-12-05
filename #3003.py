# 킹,퀸,룩,비숍,나이트,폰

white = list(map(int,input().split()))

black = [1,1,2,2,2,8]

for i in range(6):
    x = black[i] - white[i]
    print(x,end = ' ')