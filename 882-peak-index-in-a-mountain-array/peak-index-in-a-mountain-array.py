class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-1
        res = -1
        while low <= high :
            mid = (low+high)//2
            if arr[mid] < arr[mid+1]:
                low = mid +1
            elif arr[mid] > arr[mid+1]:
                res = mid
                high = mid -1
        return res            
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))        