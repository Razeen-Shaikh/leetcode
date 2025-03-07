from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        LIMIT = 10**6
        is_prime = [True] * (LIMIT + 1)
        is_prime[0] = is_prime[1] = False

        for num in range(2, int(LIMIT**0.5) + 1):
            if is_prime[num]:
                for multiple in range(num * num, LIMIT + 1, num):
                    is_prime[multiple] = False

        primes = [num for num in range(left, right + 1) if is_prime[num]]

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        ans = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i], primes[i + 1]]

        return ans
