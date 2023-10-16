from collections import deque

tools_count = deque(int(x) for x in input().split())
substances = [int(y) for y in input().split()]
challenges = [int(x) for x in input().split()]

while tools_count and substances and challenges:
    current_tool = tools_count.popleft()
    current_substance = substances.pop()
    current_score = current_tool * current_substance

    if current_score in challenges:
        challenges.remove(current_score)

    else:
        current_tool += 1
        tools_count.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostacon, ")

if tools_count:
    print(f"Tools: {', '.join(str(x) for x in tools_count)}")

if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")

if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")