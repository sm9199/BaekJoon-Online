# 약수들의 합


while(1):
    num = int(input())
    total_num = 0
    if num == -1:
        break
    arr = []
    for i in range(1,num//2+1):
        if (num%i==0):
            arr.append(i)
            total_num += i
            
    if total_num == num:
        # join 함수는 매개변수로 들어온 리스트에 있는 
        # 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수
        print(num," = "," + ".join(str(i) for i in arr), sep='')
    else:
        print(num, "is NOT perfect.")