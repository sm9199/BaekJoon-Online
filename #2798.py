# 블랙잭

card , total_num = map(int,input().split())
card_num = list(map(int,input().split()))
total = 0

for i in range(card):
    for j in range(i+1,card):
        for k in range(j+1,card):
            if card_num[i] + card_num[j] + card_num[k] > total_num:
                continue
            else:
                total = max(total,card_num[i] + card_num[j]+card_num[k])
                
print(total)