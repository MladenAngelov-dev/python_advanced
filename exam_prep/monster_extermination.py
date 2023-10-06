from collections import deque

monsters = deque(int(x) for x in input().split(","))
attack_values = [int(x) for x in input().split(',')]

total_monsters_killed = 0

while monsters and attack_values:
    current_monster = monsters.popleft()
    current_attack = attack_values.pop()

    if current_attack >= current_monster:
        total_monsters_killed += 1
        current_attack -= current_monster
        if attack_values:
            attack_values[-1] += current_attack
        elif not attack_values and current_attack > 0:
            attack_values.append(current_attack)

    elif current_attack < current_monster:
        current_monster -= current_attack
        monsters.append(current_monster)

if not monsters:
    print("All monsters have been killed!")
if not attack_values:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {total_monsters_killed}")