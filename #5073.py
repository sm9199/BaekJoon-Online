# 삼각형과 세변

while(1):
    x,y,z = map(int,input().split())
    
    if (x == y == z == 0):
        break

    
    if (x==y==z):
        print("Equilateral")
    elif 2*max(x,y,z) >= x+y+z:
        print("Invalid")    
    elif (x==y) or (x==z) or (y==z):
        print("Isosceles")
    else:
        print("Scalene")