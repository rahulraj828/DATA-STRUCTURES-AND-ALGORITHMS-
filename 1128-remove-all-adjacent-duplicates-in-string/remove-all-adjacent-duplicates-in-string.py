class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range (len(s)):
            if stack and stack[-1] == s[i]: # this means stack is not empty and last element is equals to character of str ith position :
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)            
            

        