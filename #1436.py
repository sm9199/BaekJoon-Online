# 영화감독 숌

num = int(input())
th = 666 # 666 고정
cnt = 0 # 카운트

while True:
    if '666' in str(th): 
        cnt += 1
    if cnt == num:
        print(th)
        break
    th += 1

