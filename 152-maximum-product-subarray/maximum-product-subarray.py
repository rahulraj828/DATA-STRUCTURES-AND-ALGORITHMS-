class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = 0
        max_end = nums[0]
        min_end = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = min_end * nums[i]
            v3 = max_end * nums[i]
            max_end = max(v1, max(v2,v3))
            min_end = min(v1, min(v2,v3))
            res = max(res, max(max_end, min_end))
        return res    
        