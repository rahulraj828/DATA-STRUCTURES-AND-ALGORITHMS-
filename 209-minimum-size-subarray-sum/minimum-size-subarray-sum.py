import sys
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        high = 0
        curr_sum = 0
        res = maxsize
        n = len(nums)

        while high < n:
            curr_sum += nums[high]

            while curr_sum >= target:
                length = high - low + 1
                res = min(res, length)
                curr_sum -= nums[low]
                low +=1
            high +=1
        return 0 if res ==maxsize else res        

        