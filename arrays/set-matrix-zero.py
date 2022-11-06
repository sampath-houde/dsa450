def setZeroes(matrix: list[list[int]]) -> None:
    x = 1
    y = 1
    ROWS, COLS = len(matrix), len(matrix[0])

    for c in range(COLS):
        if matrix[0][c] == 0:
            x = 0

    for r in range(ROWS):
        if matrix[r][0] == 0:
            y = 0

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    for c in range(1, COLS):
        if matrix[0][c] == 0:
            for r in range(1, ROWS):
                matrix[r][c] = 0

    for r in range(1, ROWS):
        if matrix[r][0] == 0:
            for c in range(1, COLS):
                matrix[r][c] = 0

    if x == 0:
        for r in range(COLS):
            matrix[0][r] = 0

    if y == 0:
        for c in range(ROWS):
            matrix[c][0] = 0

