# 너의 평점은..?

# dictionary을 이용한 풀이(성적 점수를 사전으로 묶음)
dictionary_grade = {'A+': 4.5 ,'A0':4.0 ,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
total_score = 0 # 총 몇학점
result_grade = 0

for _ in range(20):
    subject,score,grade = input().split()
    score = float(score) # score 자료형을 string에서 float으로 변환
    if grade != 'P':
        total_score += score # 수강한 학점을 모두 더한다
        result_grade += score * dictionary_grade[grade] # 등급과 학점을 곱한다.
        
print('%.6f'%(result_grade/total_score))
    