class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        best_ending = nums[0]
        ans = nums[0]
        for i in range (1, len(nums)): 
            v1 = best_ending + nums[i]
            v2 = nums[i]
            best_ending = max(v1, v2)
            ans = max(ans , best_ending)
        return ans    

        