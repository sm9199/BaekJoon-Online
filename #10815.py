# 숫자 카드

card_cnt_1 = int(input())
card_list_1 = list(map(int,input().split()))
card_cnt_2 = int(input())
card_list_2 = list(map(int,input().split()))

dic = {}

for i in card_list_2:
    dic[i]=0
    
for j in card_list_1:
    if j in dic:
        dic[j] = 1
        
for k in dic:
    print(dic[k], end = ' ')