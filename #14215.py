# 세 막대

a, b, c = map(int, input().split())
long_side = max(a, b, c)
short_sides = sum((a, b, c)) - long_side

while long_side >= short_sides:
    long_side -= 1
print(long_side + short_sides)