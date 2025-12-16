class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low = 0
        res = 0
        f = {}
        for high in range (len(fruits)):
            f[fruits[high]] = f.get(fruits[high], 0) +1
            while len(f) > 2:
                f[fruits[low]] -=1
                if f[fruits[low]] == 0 :
                    f.pop(fruits[low])
                low +=1
            if len(f) == 2 or len (f) < 2:
                length = high -low +1
                res = max(res , length)

        return res                        