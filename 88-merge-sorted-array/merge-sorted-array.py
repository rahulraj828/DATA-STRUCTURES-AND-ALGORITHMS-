from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Pointers for the end of valid data in nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        
        # Pointer for the end of the total array (where we write the values)
        p = m + n - 1

        # While we still have elements in nums2 to merge
        while p2 >= 0:
            # If nums1 still has elements AND nums1's element is larger
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # Otherwise, take the element from nums2
                nums1[p] = nums2[p2]
                p2 -= 1
            
            # Move the write pointer one step back
            p -= 1
            
        # Note: We don't need to check if p1 >= 0 in a separate loop.
        # If nums2 is exhausted first, the remaining elements in nums1 
        # are already in their correct places.