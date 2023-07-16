# 소인수분해

num = int(input())
div_num = 0 # 나머지
div_quoient = 0 # 몫

if num == 1:
    print('')
    
for i in range(2,num+1):
        div_num = num % i
        div_quoient = num / i 
        if (div_num == 0):
            while num % i ==0:
                print(i)
                num = num / i