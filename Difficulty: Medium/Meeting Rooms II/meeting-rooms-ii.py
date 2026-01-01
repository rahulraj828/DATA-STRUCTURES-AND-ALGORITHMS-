class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        room = 0
        res = 0
        i = j = 0
        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                room +=1
                res = max(res,room)
                i +=1
            else:
                room -=1
                j+=1
        return res        
        
        
