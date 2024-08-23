lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rows = 3
cols = 3
matrix = [[lst[i * cols + j] for j in range(cols)] for i in range(rows)]
for row in matrix:
    print(row)