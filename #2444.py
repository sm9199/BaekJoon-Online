# 별 찍기 - 7

num = int(input()) * 2 -1 # line 개수로 줄 갯수 계산
star = 1 # 별 찍을 개수를 1로 초기 설정
spacebar = int((num+1)/2) # 순서대로 앞을 기준으로 최대 띄어쓰기 개수

while star <= num:
    spacebar -= 1
    print(" "*spacebar+"*"*star)
    star += 2

while num > 1:
    num -= 2
    spacebar += 1
    print(" "*spacebar + "*"*num) 

