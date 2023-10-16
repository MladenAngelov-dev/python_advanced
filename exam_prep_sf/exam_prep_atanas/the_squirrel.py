size = int(input())
directions = input().split(', ')
hazelnuts = 0
s_row = None
s_col = None

is_game_over = False

matrix = []
for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == "s":
            s_row = row
            s_col = col

for direction in directions:
    matrix[s_row][s_col] = '*'

    if direction == "up":
        s_row -= 1
    elif direction == "down":
        s_row += 1
    elif direction == "left":
        s_col -= 1
    elif direction == "right":
        s_col += 1

    if not (0 < s_row <= size and 0 < s_col <= size):
        print("The squirrel is out of the field.")
        is_game_over = True
        break

    if matrix[s_row][s_col] == "t":
        print("Unfortunetly, the squirrel stepped on a trap...")
        is_game_over = True
        break

    if matrix[s_row][s_col] == "h":
        hazelnuts += 1
        if hazelnuts == 3:
            is_game_over = True
            print("Good job! You have collected all hazelnuts!")
            break

if hazelnuts < 3 and not is_game_over:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")