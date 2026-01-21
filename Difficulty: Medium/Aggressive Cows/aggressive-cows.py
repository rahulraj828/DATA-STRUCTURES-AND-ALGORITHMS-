class Solution:
    def cows(self , stalls ,n, k , guess):
        cows = 1
        prev = stalls[0]
        for i in range (len(stalls)) :
            dist = stalls[i] - prev
            if dist < guess :
                continue
            cows += 1
            prev = stalls[i]
        if cows >= k :
            return True
        else :
            return False
                
    def aggressiveCows(self, stalls, k):
         n = len(stalls)
         stalls.sort()
         low = 1
         high = stalls[n-1] - stalls[0]
         res = -1
         while low <= high :
             
             guess = (low+high)//2
             if self.cows(stalls , n ,k ,guess) == True :
                 res = guess
                 low = guess +1
             else :
                 high = guess -1
         return res         
        