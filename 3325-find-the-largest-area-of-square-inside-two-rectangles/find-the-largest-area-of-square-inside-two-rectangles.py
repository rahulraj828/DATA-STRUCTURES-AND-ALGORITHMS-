from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0

        for i in range(n):
            a1, b1 = bottomLeft[i]
            c1, d1 = topRight[i]

            for j in range(i + 1, n):
                a2, b2 = bottomLeft[j]
                c2, d2 = topRight[j]

                # Intersection rectangle
                left = max(a1, a2)
                bottom = max(b1, b2)
                right = min(c1, c2)
                top = min(d1, d2)

                if left < right and bottom < top:
                    side = min(right - left, top - bottom)
                    ans = max(ans, side * side)

        return ans
