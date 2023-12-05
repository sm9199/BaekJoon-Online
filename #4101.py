# 크냐?

while True:
    num1,num2 = map(int,input().split())
    sum = num1 + num2
    
    if num1 == 0 and num2 ==0:
        exit(0)
    elif num1 > num2:
        print("Yes")
    elif num1 <= num2:
        print("No")
    
