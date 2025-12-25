class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        for i in range (len(nums)):
            curr_sum += nums[i]
        for i in range (len(nums)):
            right = curr_sum - nums[i] - left 
            if left == right :
                return i
            left += nums[i]     
        return -1