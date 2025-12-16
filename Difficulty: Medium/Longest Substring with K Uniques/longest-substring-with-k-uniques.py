class Solution:
    def longestKSubstr(self, s, k):
        low = 0
        res = 0
        f = {}
        for high in range (len(s)):
            f[s[high]] = f.get(s[high], 0) +1
            while len(f) > k:
                f[s[low]] -=1
                if f[s[low]] == 0 :
                    f.pop(s[low])
                low +=1
            if len(f) == k:
                length = high -low +1
                res = max(res , length)
                
        return res if res != 0 else -1         
        