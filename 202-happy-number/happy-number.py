class Solution:
    def sum_sq(self, n):
        total = 0
        while n > 0:
            d = n % 10
            n //= 10
            total += d * d
        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while True:
            slow = self.sum_sq(slow)
            fast = self.sum_sq(fast)
            fast = self.sum_sq(fast)

            if fast == 1:
                return True
            if slow == fast:
                return False
        