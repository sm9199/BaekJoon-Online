# 설탕 배달

sugar_weight = int(input())
sugar_cnt = 0

while sugar_weight >=0:
    if sugar_weight % 5 == 0: # 5의 배수로 딱 떨어질 때
        sugar_cnt += (sugar_weight // 5)
        print(sugar_cnt) 
        break
    sugar_weight -= 3 # 만약 5의 배수가 아니면 3kg을 먼저 채우는 형식(sugar_weight - 3kg)
  
    sugar_cnt += 1 # 3kg을 채웠으니 3kg 설탕 카운트(설탕 주머니) 1을 늘림
else:
    print(-1) 