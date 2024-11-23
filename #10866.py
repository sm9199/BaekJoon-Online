# 덱
import sys

num = int(sys.stdin.readline())

for i in range(num):
    command = list(sys.stdin.readline().split())
    
    if command[0] == "push_front":
        