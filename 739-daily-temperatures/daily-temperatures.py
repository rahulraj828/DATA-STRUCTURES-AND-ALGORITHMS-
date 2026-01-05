class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*(n)  # ✅ FIX: Must be length n
        stack = []
        stack.append(n-1)
        for i in range(n-2 , -1 , -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if  not stack :
                res[i] = 0
                
            else:
                res[i] = stack[-1] - i
                

            stack.append(i)
        return res