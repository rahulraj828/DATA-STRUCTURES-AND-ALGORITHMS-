class Solution:
    def pages(self,arr,n ,limit ,stud):
        k = 1
        page = 0
        for i in range (len(arr)):
            if page + arr[i] <= limit :
                page += arr[i]
            else :
                k +=1
                page = arr[i]
                if k > stud :
                    return False
        return True            
    def findPages(self, arr, k):
        n = len(arr)
        if n < k :
            return -1
        low = high = 0
        for i in range (len(arr)) :
            low = max(low , arr[i])
            high = high + arr[i]
        res = -1
        while low <= high :
            guess = (low+high)//2
            if self.pages(arr,n,guess,k):
                res = guess
                high = guess - 1
            else :
                low = guess + 1
        return res         
        
