class Solution:
    def firstUniqChar(self, s: str) -> int:
        f= {}
        for char in s:
            if char in f :
                f[char] +=1
            else:
                f[char]  = 1

        for idx, char in enumerate(s):
            if f[char] == 1:
                return idx
        
        return -1