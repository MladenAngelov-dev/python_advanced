from collections import deque

monster_armor = deque([int(x) for x in input().split(',')])
soldier_strikes = [int(y) for y in input().split(',')]

total_kills = 0

while monster_armor and soldier_strikes:
    current_monster = monster_armor.popleft()
    current_soldier = soldier_strikes.pop()

    if current_soldier >= current_monster:
        total_kills +=1
        current_soldier -= current_monster
        if not soldier_strikes and current_soldier > 0:
            soldier_strikes.append(current_soldier)
        elif soldier_strikes:
            soldier_strikes[-1] += current_soldier
    else:
        current_monster -= current_soldier
        monster_armor.append(current_monster)
