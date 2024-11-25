# 지능형 기차2

passenger = 0
max_passenger = 0

for i in range(10):
    out_station, in_station = map(int, input().split())
    passenger += in_station - out_station
    max_passenger = max(passenger, max_passenger)
    
print(max_passenger)
