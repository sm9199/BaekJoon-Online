# 사분면 고르기

point_x = int(input())
point_y = int(input())

#제 1사분면 x,y 포인트 양수
if (point_x > 0) and (point_y > 0):
    print(1)
#제 2사분면 x 포인트 음수 , y포인트 양수
elif (point_x < 0) and (point_y > 0):
    print(2)
#제 3사분면 x,y포인트 둘다 음수
elif (point_x < 0) and (point_y < 0):
    print(3)
#제 4사분면 x 포인트 양수, y포인트 음수
elif (point_x > 0) and (point_y < 0):
    print(4)