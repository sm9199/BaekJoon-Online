# 오븐 시계
hour,min = map(int,input().split())
during_time = int(input())

if min + during_time >= 60:
    if hour+((min+during_time)//60)>=24:
        print((hour+((min+during_time)//60)-24),(min+during_time)%60)
    else:
        print(hour+(min+during_time)//60,(min+during_time)%60)
else:
    print(hour, min+during_time)