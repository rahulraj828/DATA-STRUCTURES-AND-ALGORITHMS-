class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        total_sum = nums[0]
        max_ans = nums[0]
        min_ans = nums[0]
        
        for i in range(1,len(nums)):
            total_sum += nums[i]

            max_sum = max(nums[i], max_sum + nums[i])
            max_ans = max(max_ans, max_sum)

            min_sum = min(nums[i], min_sum + nums[i])
            min_ans = min(min_ans, min_sum)

        if max_ans < 0:
            return max_ans

        return max(max_ans, total_sum - min_ans)    
           

        