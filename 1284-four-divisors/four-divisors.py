import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for n in nums:
            divisors = []

            for i in range(1, int(math.isqrt(n)) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)

                # Early stop if more than 4 divisors
                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                total_sum += sum(divisors)

        return total_sum