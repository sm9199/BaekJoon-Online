# 진법 변환 2

num1,num2 = map(int,input().split())
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ''

while num1 != 0: # num1이 0이 아닐 때 까지 반복하여
    answer += str(num_list[num1 % num2]) # 해당되는 값 자리를 answer에 단어 추가하며
    num1 //= num2 # num1 을 num2 로 나누면서 진행

print(answer[::-1]) # 처음부터 끝까지 해당되는 단어를 출력


