def next_move(command, current_row, current_col):
    if command == "up" and is_valid(current_row-1, rows):
        return current_row-1, current_col
    if command == "down" and is_valid(current_row+1, rows):
        return current_row + 1, current_col
    if command == "left" and is_valid(current_col-1, cols):
        return current_row, current_col-1
    if command == "right" and is_valid(current_col+1, cols):
        return current_row, current_col+1
    return None, None
def is_valid(value, max_value):
    return 0<= value < max_value


rows ,  cols = [int(x) for x in input().split(" ")]

matrix = []
start_row, start_col = None, None
boy_row, boy_col = None, None
line = " "

for r in range(rows):
    row = list(input())
    matrix.append(row)
    if "B" in row:
        boy_row = r
        boy_col = row.index("B")
        start_row = boy_row
        start_col = boy_col

while line:
    line = input()
    next_row, next_col = next_move(line, boy_row, boy_col)

    if next_row is None or next_col is None:
        print("The delivery is late. Order is canceled.")
        matrix[start_row][start_col] = " "
        break

    if matrix[next_row][next_col] == "*":
        continue

    if matrix[next_row][next_col] == "A":
        matrix[boy_row][boy_col] = "."
        boy_row, boy_col = next_row, next_col
        matrix[boy_row][boy_col] = "P"
        print("Pizza is delivered on time! Next order...")
        matrix[start_row][start_col] = "B"
        break

    if matrix[next_row][next_col] == "P":
        matrix[boy_row][boy_col] = "."
        boy_row, boy_col = next_row, next_col
        matrix[next_row][next_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
        continue
    if not matrix[boy_row][boy_col] == "R":
        matrix[boy_row][boy_col] = "."
    boy_row, boy_col = next_row, next_col
    matrix[boy_row][boy_col] = "."

for row in matrix:
    print(''.join(row))