def calculate_position(mat, row, col):
    if row < 0:
        row = len(mat) - 1
    if col < 0:
        col = len(mat[0]) - 1
    if row >= len(mat):
        row = 0
    if col >= len(mat[0]):
        col = 0

    return row, col


n = int(input())

matrix = []
ship = []
fish = 0
has_fallen_into_whirlpool = False
whirlpool = []


for row_index in range(n):
    row_data = list(input().strip())
    if "S" in row_data:
        ship = [row_index, row_data.index("S")]
    if "W" in row_data:
        whirlpool = [row_index, row_data.index('W')]
    matrix.append(row_data)

while True:
    command = input().strip()
    current_row, current_col = ship

    if command == "up":
        row, col = calculate_position(matrix, current_row - 1, current_col)
    elif command == "down":
        row, col = calculate_position(matrix, current_row + 1, current_col)
    elif command == "right":
        row, col = calculate_position(matrix, current_row, current_col + 1)
    elif command == "left":
        row, col = calculate_position(matrix, current_row, current_col - 1)

    if command == "collect the nets":
        break

    if matrix[row][col].isdigit():
        fish += int(matrix[row][col])
        matrix[row][col] = '-'
    elif matrix[row][col] == "W":
        has_fallen_into_whirlpool = True
        break

    matrix[current_row][current_col] = '-'
    matrix[row][col] = 'S'
    ship = [row, col]

if has_fallen_into_whirlpool:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
          f" Last coordinates of the ship: [{whirlpool[0]}, {whirlpool[1]}]")
elif fish >= 20:
    print("Success! You managed to reach the quota!")
    print(f"Amount of fish caught: {fish} tons.")
else:
    lack_of_fish = 20 - fish
    print(f"You didn't catch enough fish and didn't reach the quota!"
          f" You need {lack_of_fish} tons of fish more.")
    print(f"Amount of fish caught: {fish} tons.")

if not has_fallen_into_whirlpool:
    for row in matrix:
        print("".join(row))
