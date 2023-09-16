n = int(input())
my_stack = []

for _ in range(n):
    command = input().split()
    if command[0] == "1":
        number = int(command[1])
        my_stack.append(number)
    elif my_stack:
        if command[0] == "2":
            my_stack.pop()
        elif command[0] == "3":
            print(max(my_stack))
        elif command[0] == "4":
            print(min(my_stack))

while my_stack:
    print(my_stack.pop(), end="")
    if my_stack:
        print(", ", end="")