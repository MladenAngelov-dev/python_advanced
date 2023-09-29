numbers = [line.split() for line in input().split("|")]
print(*[' '.join(sub_line) for sub_line in numbers[:: -1] if sub_line])