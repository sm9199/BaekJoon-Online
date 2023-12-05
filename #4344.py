# 평균은 넘겠지???

N = int(input())

for _ in range(N):
    num_students = list(map(int,input().split()))
    avg = sum(num_students[1:])/num_students[0]
    count = 0 # 평균 넘는 학생들 카운트함
    for score in num_students[1:]:
        if score > avg:
            count +=1
        rate = count/num_students[0] * 100
    print("{:.3f}%".format(rate))