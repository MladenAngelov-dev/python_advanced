from collections import deque

tools = deque(int(x) for x in input().split())
substance = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while challenges and substance:
    current_tool = tools.popleft()
    current_substance = substance[-1]
    score = current_substance * current_tool

    if score in challenges:
        challenges.remove(score)
        substance.pop()
        continue

    current_tool += 1
    tools.append(current_tool)
    substance[-1] -= 1
    if substance[-1]== 0:
        substance.pop()

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")
if substance:
    print(f"Substances: {', '.join([str(x) for x in substance])}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")