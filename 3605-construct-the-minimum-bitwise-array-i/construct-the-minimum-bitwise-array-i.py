class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
                continue

            # count trailing ones
            t = 0
            y = x
            while y & 1:
                t += 1
                y >>= 1

            ans.append(x - (1 << (t - 1)))

        return ans
