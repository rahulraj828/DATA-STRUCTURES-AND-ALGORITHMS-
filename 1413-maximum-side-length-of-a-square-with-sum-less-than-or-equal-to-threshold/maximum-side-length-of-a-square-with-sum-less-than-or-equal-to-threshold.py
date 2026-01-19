from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Build prefix sum matrix
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = (
                    mat[i][j]
                    + ps[i][j + 1]
                    + ps[i + 1][j]
                    - ps[i][j]
                )

        def exists_square(k: int) -> bool:
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    square_sum = (
                        ps[i + k][j + k]
                        - ps[i][j + k]
                        - ps[i + k][j]
                        + ps[i][j]
                    )
                    if square_sum <= threshold:
                        return True
            return False

        low, high = 0, min(m, n)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if exists_square(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
