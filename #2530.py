# 인공지능 시계

hour,min,sec = map(int,input().split())
during_sec = int(input())

sec += during_sec
min += sec // 60
hour += min // 60
print(hour%24,min%60,sec%60)