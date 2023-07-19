# 단어 정렬


# ver.1 <중복을 생각 못한 코드>

# word_num = int(input())
# word_list = []

# for _ in range(word_num):
#     word = input()
#     word_list.append(word)
    
# word_list.sort()
# word_list.sort(key = len)

# for i in word_list:
#     print(i)  

# ver.2 <중복을 고려해보자>

word_num = int(input())
word_list = []

for _ in range(word_num):
    word = input()
    word_list.append(word)

set_word_list = set(word_list)   
word_list = list(set_word_list) 
word_list.sort()
word_list.sort(key = len)

for i in word_list:
    print(i)  
