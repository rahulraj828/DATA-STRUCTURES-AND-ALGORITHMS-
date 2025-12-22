#User function Template for python3


class Solution:
    def smallestSumSubarray(self, A, N):
        i = 0
        ans = A[0]
        best_end = A[0]
        for i in range (1 , N):
            v1 = best_end + A[i]
            v2 = A[i]
            best_end = min(v1 ,v2)
            ans = min(best_end ,ans)
        return ans    
            
            