from collections import deque

fuel = [int(x) for x in input().split()]
consumption = deque([int(x) for x in input().split()])
needed_fuel = deque([int(x) for x in input().split()])

altitude = 0
is_fail = False
reached = []

while fuel:
    current_fuel = fuel.pop()
    current_consumption = consumption.popleft()
    target = needed_fuel.popleft()

    current_fuel_need = current_fuel - current_consumption

    if current_fuel_need >= target:
        altitude += 1
        print(f"John has reached: Altitude {altitude}")
        reached.append(altitude)
    else:
        altitude += 1
        print(f"John did not reach: Altitude {altitude}")
        is_fail = True
        break

if is_fail:
    print("John failed to reach the top.")
    if len(reached) == 0:
        print("John didn't reach any altitude.")
    else:
        print("Reached altitudes: " + ", ".join([f"Altitude {alt}" for alt in reached]))
else:
    print("John has reached all the altitudes and managed to reach the top!")
