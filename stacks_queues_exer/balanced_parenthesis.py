from collections import deque

parenthesis = deque(input())
open_parenthesis = deque()

while parenthesis:
    current_parentesis = parenthesis.popleft()

    if current_parentesis in "({[":
        open_parenthesis.append(current_parentesis)
    elif not open_parenthesis:
        print("NO")
        break
    else:
        if f"{open_parenthesis.pop() + current_parentesis}" not in "(){}[]":
            print("NO")
            break
else:
    print("YES")