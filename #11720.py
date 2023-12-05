# 숫자의 합

num = int(input())
nums = list(input())
total_num = 0

for i in range(num):
    total_num += int(nums[i])
    
print(total_num)
    