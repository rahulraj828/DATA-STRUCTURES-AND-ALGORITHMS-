class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        f = {0:1}
        res = 0
        for i in nums:
            curr_sum += i
            ques = curr_sum - k
            res += f.get(ques, 0)
            f[curr_sum] = f.get(curr_sum, 0) + 1
        return res    


        