# 삼각형 외우기

angle_1st = int(input())
angle_2nd = int(input())
angle_3rd = int(input())

angle_sum = angle_1st + angle_2nd + angle_3rd

if angle_sum == 180:
    if (angle_1st == 60) and (angle_2nd == 60) and (angle_3rd == 60):
        print("Equilateral")
    elif (angle_1st == angle_2nd) or (angle_1st == angle_3rd) or (angle_2nd == angle_3rd): 
        print("Isosceles")
    elif (angle_1st != angle_2nd != angle_3rd): 
        print("Scalene")
else:
    print("Error")