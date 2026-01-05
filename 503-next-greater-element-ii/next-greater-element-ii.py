class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        for i in range(n-2 , -1 , -1):
            stack.append(nums[i])
        for i in range(n-1 , -1 , -1):    
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if not stack :
                res[i] = -1
            else :
                res[i] = stack[-1]
            stack.append(nums[i])
        return res            

        