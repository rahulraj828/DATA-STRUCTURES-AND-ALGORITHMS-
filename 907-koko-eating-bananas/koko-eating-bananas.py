class Solution:
    def sped(self ,piles: List[int] , k: int):
        hour = 0
        for p in piles:
            hour += (p + k - 1) // k   # integer ceiling
        return hour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = -1
        while low <= high :

            guess = (low+high)//2
            time = self.sped(piles, guess)
            if time > h :
                low = guess + 1
            else :
                res = guess
                high = guess - 1
        return res            

        