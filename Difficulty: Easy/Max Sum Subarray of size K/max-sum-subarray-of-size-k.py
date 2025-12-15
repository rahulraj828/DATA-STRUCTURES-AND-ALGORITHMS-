class Solution:
    def maxSubarraySum(self, arr, k):
        low = 0
        high = k-1
        n = len(arr)
        res = 0
        curr_sum = 0
        for i in range (k):
            curr_sum = curr_sum + arr[i]
            res = curr_sum
        while high < n-1:
            
            curr_sum = curr_sum - arr[low]
            low +=1
            high +=1
            curr_sum = curr_sum + arr[high]
            res = max(res, curr_sum)
        return res        