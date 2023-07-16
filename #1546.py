# 평균

subject = int(input())
grade = list(map(int,input().split()))

max_grade = max(grade)

new_score = []

for i in range(subject):
    new_score.append(grade[i]/max_grade*100)
avg = sum(new_score)/subject

print(avg)
