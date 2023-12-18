# 파댕이컵 A번 유치원생 파댕이

import sys

Time1 = int(sys.stdin.readline())
Num_candy = int(sys.stdin.readline())
candy_flavor = list(map(int,input().split()))
    
if sum(candy_flavor) < Time1:
   print("Padaeng_i Cry")
else:
    print("Padaeng_i Happy") 