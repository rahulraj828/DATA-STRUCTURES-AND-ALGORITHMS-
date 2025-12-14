class Solution:
    def countTriplets(self, n, sum, arr):
        arr.sort()
        count = 0
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right :
                target = arr[i]+arr[left]+arr[right]
                if target >= sum:
                    right = right-1
                else:
                    count = count+(right-left)
                    left =left+1
                
        return count   
        