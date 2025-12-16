class Solution:
    def countTriplets(self, n, sum, arr):
        arr.sort()
        n = len(arr)
        ans = 0
        for i in range (n-2):
            left = i+1
            right = n-1
            
            while left < right:
                curr_sum = arr[i]+arr[left]+arr[right]
                if curr_sum >= sum :
                    right -=1
                else:
                    ans = ans+right -left
                    left +=1
        return ans         
                
            