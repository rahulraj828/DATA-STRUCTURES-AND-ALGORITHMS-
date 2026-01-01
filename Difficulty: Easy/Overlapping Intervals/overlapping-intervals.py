class Solution:
    def isIntersect(self, intervals):
       intervals.sort(key = lambda x : x[0])
       start1 , end1 = intervals[0]
       for i in range (1,len(intervals)):
           start2 , end2 = intervals[i]
           if end1 >= start2:
               return True
           start1 = start1
           end1 = max(end1,end2)
               
       