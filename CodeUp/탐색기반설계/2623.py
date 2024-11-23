# 2623 : 최대공약수 구하기

n1, n2 = map(int, input().split())

def gcd(n1,n2):
    if n1 < n2:
        n1, n2 = n2, n1
        
    if n2 == 0:
        return n1

    if n1 % n2 == 0:
        return n2
    
    else:
        return gcd(n2, n1%n2)
    
    
print(gcd(n1,n2))