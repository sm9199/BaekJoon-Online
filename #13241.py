# 최소 공배수(유클리드 호제법)

import sys

def gcd(num1, num2):
    a, b = num1, num2
    while True:
        b = b % a
        a, b = b, a
        if a == 0:
            return b


a, b = map(int, sys.stdin.readline().split())
print(a * b // gcd(a, b))