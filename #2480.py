# 주사위 세개

dice_1,dice_2,dice_3 = map(int,input().split())

if dice_1 == dice_2 == dice_3:
    print(10000+(dice_1*1000))
elif dice_1 == dice_2 or dice_1==dice_3:
    print(1000+(dice_1*100))
elif dice_2 == dice_3:
    print(1000+(dice_2*100))
elif dice_1 != dice_2 != dice_3:
    if dice_1>dice_2 and dice_1>dice_3:
        print(dice_1*100)
    elif dice_2>dice_1 and dice_2>dice_3:
        print(dice_2*100)
    elif dice_3>dice_1 and dice_3 >dice_2:
        print(dice_3*100)