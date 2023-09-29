n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input().split()

while command[0] != "END":
    current_command = command[0]
    row = int(command[1])
    col = int(command[2])
    number = int(command[3])

    if not (0 <= row < n and 0 <= col < n):
        print("Invalid coordinates")
    elif command[0] == "Add":
        matrix[row][col] += number
    elif command[0] == "Subtract":
        matrix[row][col] -= number

    command = input().split()

[print(*row) for row in matrix]