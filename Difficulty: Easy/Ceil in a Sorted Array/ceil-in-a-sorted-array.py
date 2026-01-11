#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        low = 0
        high = len(arr) - 1
        res = -1
        while low <= high :
            guess = (low+high)//2
            if arr[guess] < x :
                low = guess +1
            else :
                res = guess
                high = guess - 1
        return res        
