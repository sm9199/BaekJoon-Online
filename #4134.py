# 다음 소수
import math

def prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if x % i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    num = int(input())
    while True:
        if prime_number(num):
            print(num)
            break
        else:
            num += 1