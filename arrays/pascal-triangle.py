def generate(numRows: int) -> list[list[int]]:
    ans = []
    for r in range(numRows):
        colList = []
        c = 0
        while c <= r:
            if c == 0 or c == r:
                colList.append(1)
            elif c<r:
                colList.append(ans[r-1][c - 1] + ans[r-1][c])
            else:
                break
            c = c + 1
        ans.append(colList)
    return ans


generate(5)
