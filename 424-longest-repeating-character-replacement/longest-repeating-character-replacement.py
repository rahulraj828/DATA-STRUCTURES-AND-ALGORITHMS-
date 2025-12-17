class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        low = 0
        high = 0
        res = 0
        f = {}
        for high in range (len(s)):
            f[s[high]]  = f.get(s[high] , 0)+1
            length = high - low +1
            max_cnt = max(f.values())
            diff = length - max_cnt
            while diff > k :
                f[s[low]] -=1
                low +=1
                max_cnt = max(f.values())

                length = high - low +1
                diff = length - max_cnt
            if diff < k or diff == k :
                length = high - low +1
                res = max(res , length)
        return res            

        