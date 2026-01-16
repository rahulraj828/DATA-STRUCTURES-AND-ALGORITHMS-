class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int,
                            hFences: List[int],
                            vFences: List[int]) -> int:
        MOD = 10**9 + 7

        # Include boundary fences
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])

        # All possible vertical distances (from horizontal fences)
        vertical_distances = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                vertical_distances.add(h[j] - h[i])

        # All possible horizontal distances (from vertical fences)
        horizontal_distances = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                horizontal_distances.add(v[j] - v[i])

        # Find the largest possible square side
        common = vertical_distances & horizontal_distances
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD
