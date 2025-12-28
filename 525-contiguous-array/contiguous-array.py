class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        f = {}
        one = 0
        zero = 0
        res = 0
        for i in range (len(nums)):
            if nums[i] == 0:
                zero +=1
            else:
                one +=1
            diff = zero - one
            if diff == 0 :
                res = max(res, i+1)
                continue
            if diff in f:
                res = max(res, i - f[diff])
            else:
                f[diff] = i
        return res              

        