matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("First row:", matrix[0])

last_column = []
for row in matrix:
    last_column.append(row[-1])
print("Last column:", last_column)

total = 0
for row in matrix:
    for value in row:
        total += value

print("Sum =", total)