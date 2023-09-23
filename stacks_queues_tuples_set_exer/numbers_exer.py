first_line = set(int(x) for x in input().split())
second_line = set(int(x) for x in input().split())

commands = {
    "Add First": lambda x: [first_line.add(el) for el in x],
    "Add Second": lambda x: [second_line.add(el) for el in x],
    "Remove First": lambda x: [first_line.discard(el) for el in x],
    "Remove Second": lambda x: [second_line.discard(el) for el in x],
    "Check Subset": lambda x: print(first_line.issubset(second_line) or second_line.issubset(first_line)),

}

for _ in range(int(input())):
    first_part, second_part , *data = input().split()
    command = first_part + " " + second_part

    commands[command](int(x) for x in data)

print(*sorted(first_line), sep=", ")
print(*sorted(second_line), sep=", ")