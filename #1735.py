# 분수 합

def gcd(x,y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y        
    return y

num1, num2 = map(int, input().split())
num3, num4 = map(int, input().split())
result = gcd(num1*num4 + num2*num3 , num2*num4)
print((num1*num4 + num2*num3)//result, num2*num4//result)

