# 달팽이는 올라가고 싶다

climb , slide , height = map(int,input().split())

if (height-slide)%(climb-slide) ==0:
    print((height-slide)//(climb-slide))
else:
    print((height-slide)//(climb-slide)+1)