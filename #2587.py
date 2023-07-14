num_list = []

for i in range(5):
    num = int(input())
    num_list.append(num)
    num_list.sort()
    
num_avg = int(sum(num_list) / 5)
num_mid = num_list[2]

print(num_avg)
print(num_mid)


