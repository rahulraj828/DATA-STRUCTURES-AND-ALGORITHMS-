class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while nums[i] != nums[i-1]:
            i +=1
        return nums[i]    
        