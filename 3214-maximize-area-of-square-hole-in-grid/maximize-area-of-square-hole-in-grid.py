from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        def max_gap(bars: List[int]) -> int:
            if not bars:
                return 1
            
            bars.sort()
            longest = curr = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr += 1
                else:
                    curr = 1
                longest = max(longest, curr)
            
            # removing k consecutive bars creates a gap of k + 1
            return longest + 1
        
        max_h = max_gap(hBars)
        max_v = max_gap(vBars)
        
        side = min(max_h, max_v)
        return side * side
