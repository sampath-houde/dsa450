def rotate(matrix: list[list[int]]) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])
    for r in range(ROWS):
        for c in range(r, COLS):
            temp = 0
            temp = matrix[r][c]
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = temp

    start = 0
    end = COLS - 1
    print(matrix)
    for r in range(ROWS):
        for c in range(COLS % 2):
            temp = matrix[r][start]
            matrix[r][start] = matrix[r][end]
            matrix[r][end] = temp
