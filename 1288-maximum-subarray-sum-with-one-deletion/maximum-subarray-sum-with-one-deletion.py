class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nodelete = nums[0]
        onedelete = None
        res = nums[0]
        for i in range(1, len(nums)):
            prev_nodelete = nodelete
            prev_onedelete = onedelete
            nodelete = max(nodelete+nums[i] , nums[i])
            if prev_onedelete == None:
                v2 = nums[i]
            else:
                v2 = prev_onedelete + nums[i]
            onedelete = max(v2, prev_nodelete)  
            res = max(res , max(onedelete , nodelete))
        return res     


