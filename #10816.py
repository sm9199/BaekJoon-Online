# 숫자 카드 2
import sys

n = int(sys.stdin.readline()) # 첫번째 줄에 몇장의 카드있는지 입력
card_lst_1 = [*map(int,input().split())] # 리스트 형식으로 카드 담음
m = int(sys.stdin.readline()) # 세번째 줄에 몇장의 카드 판별할 것인지 입력 
card_lst_2 = [*map(int,input().split())] # 리스트형식으로 어떤 카드가 몇장 있는지 판별하는 도구 

count = {} # dictionary 형식으로 담을 count 변수 생성

# 변수 card를 이용해 card_lst_1에 담겨진 원소만큼 반복해서 몇장있는지 갱신함.
for card in card_lst_1: 
    if card in count: # 만약 card 숫자가 중복(포함되있을 시) 1을 증가시킴.
        count[card] += 1
    else: # 만약 card 숫자가 처음 갱신한다면 1로 설정
        count[card] = 1
        
# 변수 check을 이용해 card_lst_2에 담겨진 원소가 몇개 있는지 판별하기 위해 count함수를 사용하여 갯수 판단.
for check in card_lst_2: # card_lst_2 만큼 반복
    total_card = count.get(check) # count 딕셔너리에 담겨지지 않은 변수는 0으로 초기화
    if total_card == None:
        print(0,end=" ")
    else: # count 딕셔너리에 담긴 원소는 갯수를 출력하게 함.
        print(total_card , end=" ")
