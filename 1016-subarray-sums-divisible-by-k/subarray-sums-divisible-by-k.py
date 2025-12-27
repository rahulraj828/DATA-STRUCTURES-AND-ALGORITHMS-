class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curr_sum = 0 
        res = 0 
        f = {0:1}
        for i in range (len(nums)):
            curr_sum += nums[i]
            rem = curr_sum % k
            if rem <0 :
                rem = rem +k
            res += f.get(rem , 0) 
            f[rem] = f.get(rem, 0) + 1
            
        return res        
        