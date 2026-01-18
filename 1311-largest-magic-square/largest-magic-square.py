from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Prefix sums
        row = [[0]*(n+1) for _ in range(m)]
        col = [[0]*n for _ in range(m+1)]
        diag1 = [[0]*(n+1) for _ in range(m+1)]
        diag2 = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[i+1][j] = col[i][j] + grid[i][j]
                diag1[i+1][j+1] = diag1[i][j] + grid[i][j]
                diag2[i+1][j] = diag2[i][j+1] + grid[i][j]

        def row_sum(r, c, k):
            return row[r][c+k] - row[r][c]

        def col_sum(r, c, k):
            return col[r+k][c] - col[r][c]

        def diag1_sum(r, c, k):
            return diag1[r+k][c+k] - diag1[r][c]

        def diag2_sum(r, c, k):
            return diag2[r+k][c] - diag2[r][c+k]

        max_k = min(m, n)

        for k in range(max_k, 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = row_sum(i, j, k)

                    # Check diagonals
                    if diag1_sum(i, j, k) != target or diag2_sum(i, j, k) != target:
                        continue

                    valid = True

                    # Check rows and columns
                    for t in range(k):
                        if row_sum(i + t, j, k) != target or col_sum(i, j + t, k) != target:
                            valid = False
                            break

                    if valid:
                        return k

        return 1
