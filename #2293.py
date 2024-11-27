# 동전 1

n, k = map(int, input().split())

lst = []

for _ in range(n):
    lst.append(int(input()))

# <dp[1] = 1>    
# 1원 = 1

# <dp[2] = 2>
# 2원 => 1+1
# 2원 => 2

# <dp[3] = 2>
# 3원 => 1+1+1
# 3원 => 2+1 / 1+2

# <dp[4] = 3>
# 4원 => 1+1+1+1
# 4원 => 2+2
# 4원 => 1+1+2 / 1+2+1 / 2+1+1

# 결론 : dp[i] = dp[i] + dp[i-coin]

dp = [0 for i in range(k+1)]
dp[0] = 1

for x in lst:
    for i in range(x, k+1):
##        dp[i] += dp[i - x]
        
print(dp[k])