class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        high = 0
        res = 0
        f = {}
        for high in range(len(s)):
            f[s[high]] = f.get(s[high], 0) +1
            k = high-low +1
            while len(f) < k:
                f[s[low]] -=1
                if f[s[low]] == 0:
                    f.pop(s[low])
                low +=1
                k = high - low +1
            length = high - low +1
            res = max(res , length)
        return res            




        