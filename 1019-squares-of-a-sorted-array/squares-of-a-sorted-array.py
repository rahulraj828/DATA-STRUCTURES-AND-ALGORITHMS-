class Solution:
    from typing import List

    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        neg = []
        pos = []
        for i in range(size):
            if nums[i] >= 0 :
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        if len(pos) == 0:   
            for i in range(len(pos)):
                nums[i]=nums[i]*nums[i]
            nums.reverse()

        if len(neg) == 0 : 
            for i in range(len(neg)):
                nums[i]=nums[i]*nums[i]
                nums
        
        
        for i in range(len(pos)):    
            pos[i] = pos[i]*pos[i]

         

        for i in range(len(neg)):
            neg[i] = neg[i]*neg[i] 
        neg.reverse()
        
        i = 0
        j = 0
        res = []
        k  = 0
        while i<len(pos) and j<len(neg):
            if pos[i] <= neg[j]:
                res.insert(k, (pos[i]))
                i = i+1
                k = k+1
            
            else:
                res.insert(k, (neg[j]))
                j = j+1
                k = k+1

        
        while i<len(pos):
            res.insert(k, (pos[i]))
            i = i+1
            k = k+1
        while j<len(neg):
            res.insert(k, (neg[j]))
            j = j+1 
            k = k+1   
        return res    







                


                         



        