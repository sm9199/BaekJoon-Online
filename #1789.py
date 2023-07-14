num = int(input())
total_num = 0
num_count = 0

for i in range(1,num+1):
    total_num += i
    num_count += 1
    if total_num>num:
        num_count -= 1
        break
    
print(num_count)