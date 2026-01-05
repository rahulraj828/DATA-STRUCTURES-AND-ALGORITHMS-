class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []
        for c in s :
            if not stack or stack[-1][0] != c:
                stack.append([c , 1])
                continue
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return  "".join(char * count for char, count in stack)
