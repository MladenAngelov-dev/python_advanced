def swap(comm, indexes):
    if valid_index(indexes) and comm == "swap" and len(indexes) == 4:
        row1, col1, row2, col2 = indexes

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(j) for j in matrix], sep="\n")
    else:
        print("Invalid input!")


def valid_index(indexes):
    return {indexes[0], indexes[2]}.issubset(valid_rows) and {indexes[1], indexes[3]}.issubset(valid_cols)


rows,  cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    swap(command, info)