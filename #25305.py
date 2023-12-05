# 커트라인

stu_num , cut_line = map(int,input().split())
score = list(map(int,input().split()))

score.sort(reverse=True)

print(score[cut_line-1])