import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0]+nums[1]+nums[2]
        min_int = sys.maxsize

        for i in range(n-2):
            left = i+1
            right = n-1

            while left<right:
                sum = nums[i]+nums[left]+nums[right]

                if sum == target:
                    return target
                if sum< target:
                    left = left+1
                else:
                    right = right-1

                diff_target = abs(sum - target)
                if diff_target < min_int :
                    res = sum
                    min_int = diff_target

        return res                     


        