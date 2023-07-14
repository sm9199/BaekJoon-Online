# 빠른 A + B 
# 속도 측면에서는 input()보다 sys.stdin.readline()을 사용하는 것이 더욱 빠르다!
# input()대신 sys.sydin.readline()을 사용하면 시간 초과 문제를 해결할 수 있다.
import sys 

item = int(sys.stdin.readline())

for i in range(item):
    num1,num2 = map(int,sys.stdin.readline().split())
    print(num1+num2)