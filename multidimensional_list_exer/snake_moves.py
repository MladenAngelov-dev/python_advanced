from collections import deque

rows, cols = [int(x) for x in input().split()]
text = list(input())

text_copy = deque(text)

for row in range(rows):
    while len(text_copy) < cols:
        text_copy.extend(text)

    if row % 2 == 0:
        print(*[text_copy.popleft() for _ in range(cols)], sep="")
    else:
        print(*[text_copy.popleft() for _ in range(cols)][::-1], sep="")