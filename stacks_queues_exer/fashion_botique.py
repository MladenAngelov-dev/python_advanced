clothes = [int(x) for x in input().split()]
racks_capacity = int(input())

counter = 1
current_rack_capacity = racks_capacity

while clothes:
    cloth = clothes.pop()
    if current_rack_capacity >= cloth:
        current_rack_capacity -= cloth
    else:
        counter += 1
        current_rack_capacity = racks_capacity - cloth

print(counter)