# # 촤소 공배수

# num = int(input())

# for i in range(num):
    
#     n1, n2 = map(int, input().split())

#     for j in range(max(n1,n2), (n1*n2)+1):
#         if j % n1 ==0 and j % n2 == 0:
#            print(j)    

import sys

def gcd(num1, num2):
    a, b = num1, num2
    while True:
        b = b % a
        a, b = b, a
        if a == 0:
            return b

for n in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    print(a * b // gcd(a, b))