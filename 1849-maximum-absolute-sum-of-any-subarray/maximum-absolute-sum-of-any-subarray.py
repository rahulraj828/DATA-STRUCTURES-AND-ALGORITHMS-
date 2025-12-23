class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr = 0
        res = 0
        premax ,premin = 0, 0
        for i in nums:
            curr += i
            res = max(res , abs(curr - premax) , abs(curr - premin))
            premin = min(premin , curr)
            premax = max(premax, curr)
        return res    
        