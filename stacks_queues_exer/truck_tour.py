from collections import deque

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

tank_gas = 0
index = 0
pumps_copy = pumps_data.copy()

while pumps_copy:
    gas, distance = pumps_copy.popleft()
    tank_gas += gas

    if tank_gas >= distance:
        tank_gas -= distance
    else:
        pumps_data.rotate(-1)
        pumps_copy = pumps_data.copy()
        index +=1
        tank_gas = 0

print(index)