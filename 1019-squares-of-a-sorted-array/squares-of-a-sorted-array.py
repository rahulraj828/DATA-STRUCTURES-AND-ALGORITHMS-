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

        if len(pos) == 0:    # for  all negative values in array:
            for i in range(len(pos)):
                nums[i]=nums[i]*nums[i]
            nums.reverse()

        if len(neg) == 0 :   # for  all positive values in array:
            for i in range(len(neg)):
                nums[i]=nums[i]*nums[i]
                nums
        # now for both cases (array containing both negative and positive values):
        # we have divided the array into positive and negative array:
        
        for i in range(len(pos)):    # for positive array elements:
            pos[i] = pos[i]*pos[i]

         

        for i in range(len(neg)):
            neg[i] = neg[i]*neg[i] 
        neg.reverse()
        # now taking pointer i and pointer j for iteration of both array to merge:
        i = 0
        j = 0
        res = []
        k  = 0 # for index of new array:
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







                


                         



        