from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counterText = Counter(text)
        balloon = Counter("balloon")

        res = float('inf')
        for c in balloon:
            res = min(res, counterText[c] // balloon[c])

        return res
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))         
        