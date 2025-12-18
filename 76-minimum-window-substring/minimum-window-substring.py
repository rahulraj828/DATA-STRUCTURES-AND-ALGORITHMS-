from collections import Counter
from sys import maxsize

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        have = {}
        required = len(need)
        formed = 0

        low = 0
        res_len = maxsize
        res_start = 0

        for high in range(len(s)):
            char = s[high]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while formed == required:
                window_len = high - low + 1
                if window_len < res_len:
                    res_len = window_len
                    res_start = low

                left_char = s[low]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                low += 1

        return "" if res_len == maxsize else s[res_start:res_start + res_len]
