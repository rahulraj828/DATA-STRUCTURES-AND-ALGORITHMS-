class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg = 0
        mn = float('inf')

        for row in matrix:
            for val in row:
                if val < 0:
                    neg += 1
                total += abs(val)
                mn = min(mn, abs(val))

        if neg % 2 == 0:
            return total
        else:
            return total - 2 * mn
        